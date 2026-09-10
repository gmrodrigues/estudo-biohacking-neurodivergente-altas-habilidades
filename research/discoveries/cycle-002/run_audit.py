"""Audit cycle 001 selection, weights, and full-design Taylor covariance with svy."""
from __future__ import annotations
import hashlib
import importlib.metadata
import importlib.util
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import patsy
import polars as pl
import svy
from scipy import stats
from statsmodels.stats.multitest import multipletests

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
PREVIOUS = OUT.parent / 'cycle-001'
spec = importlib.util.spec_from_file_location('cycle001', PREVIOUS / 'run_analysis.py')
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
PHQ = ['DPQ010','DPQ020','DPQ040','DPQ050','DPQ060','DPQ070','DPQ080','DPQ090']
COMMON = [('SEX','RIAGENDR',[1,2]),('RACE','RIDRETH3',[1,2,3,4,6,7]),
          ('EDUC','DMDEDUC2',[1,2,3,4,5])]
TABLES = {'H1':['DR1TOT_L','SLQ_L'], 'H2':['SLQ_L','PAQ_L','DPQ_L'],
          'H3':['DR1TOT_L','DSQTOT_L','SLQ_L']}


def weight_summary(w):
    w = np.asarray(w, float)
    if not len(w) or np.any(w <= 0) or not np.isfinite(w).all():
        raise ValueError('Expected nonempty positive finite weights')
    return {'n':len(w), 'sum':float(w.sum()), 'min':float(w.min()),
            'p50':float(np.quantile(w,.5)), 'p90':float(np.quantile(w,.9)),
            'p99':float(np.quantile(w,.99)), 'max':float(w.max()),
            'cv':float(w.std(ddof=0)/w.mean()),
            'kish_n':float(w.sum()**2/np.square(w).sum()),
            'top_1pct_weight_share':float(np.sort(w)[-max(1,int(np.ceil(len(w)*.01))):].sum()/w.sum())}


def prepare(h, tables):
    frame=tables['DEMO_L'].copy()
    flow=[{'step':'DEMO todos','remaining':len(frame),'excluded':0}]
    prev=len(frame)
    # Keep the full frame for design; only count joins in the adult domain.
    present=frame.RIDAGEYR.ge(18)
    flow.append({'step':'idade ≥18','remaining':int(present.sum()),'excluded':prev-int(present.sum())})
    for name in TABLES[h]:
        incoming=tables[name].copy()
        assert incoming.SEQN.is_unique
        fresh=[c for c in incoming if c not in frame or c=='SEQN']
        marker='present_'+name
        incoming[marker]=True
        frame=frame.merge(incoming[fresh+[marker]],on='SEQN',how='left',validate='one_to_one')
        before=int(present.sum()); present &= frame[marker].fillna(False).astype(bool)
        flow.append({'step':'ligação '+name,'remaining':int(present.sum()),'excluded':before-int(present.sum())})
    frame['AGE10']=(frame.RIDAGEYR-45)/10
    frame['AGE10_SQ']=frame.AGE10**2
    for target,source,values in COMMON: frame[target]=frame[source].where(frame[source].isin(values))
    frame['PIR']=frame.INDFMPIR.where(frame.INDFMPIR.between(0,5))
    raw_rules=[(source,frame[source].isin(values)) for _,source,values in COMMON]
    raw_rules += [('INDFMPIR',frame.INDFMPIR.between(0,5)),('SLD012',frame.SLD012.notna())]
    if h in ('H1','H3'):
        frame['ENERGY1000']=frame.DR1TKCAL/1000
        raw_rules += [('DR1TKCAL',frame.DR1TKCAL.notna())]
    if h=='H1':
        frame['CAFF100']=frame.DR1TCAFF/100
        frame['CAFF_X_AGE']=frame.CAFF100*frame.AGE10
        raw_rules += [('DR1TCAFF',frame.DR1TCAFF.notna())]
    if h=='H2':
        frame['PHQ8_NOSLEEP']=frame[PHQ].where(frame[PHQ].isin([0,1,2,3])).sum(axis=1,min_count=8)
        frame['SED_HOURS']=frame.PAD680.where(frame.PAD680.between(0,1380))/60
        frame['SLEEP_CAT']=old.sleep_categories(frame.SLD012)
        raw_rules += [('PAD680',frame.PAD680.between(0,1380))]
        raw_rules += [(c,frame[c].isin([0,1,2,3])) for c in PHQ]
    if h=='H3':
        frame['DIET_MAG100']=frame.DR1TMAGN/100
        frame['SUPP_MAG_UNQUANT']=((frame.DSD010==1)&frame.DSQTMAGN.isna()).astype(float)
        frame['SUPP_MAG100']=frame.DSQTMAGN.fillna(0)/100
        frame.loc[~frame.DSD010.isin([1,2]),['SUPP_MAG100','SUPP_MAG_UNQUANT']]=np.nan
        raw_rules += [('DR1TMAGN',frame.DR1TMAGN.notna()),('DSD010',frame.DSD010.isin([1,2]))]
    weight='WTMEC2YR' if h=='H2' else 'WTDRD1'
    raw_rules += [(weight,frame[weight].gt(0)),('SDMVSTRA',frame.SDMVSTRA.notna()),('SDMVPSU',frame.SDMVPSU.notna())]
    joined=present.copy(); retained=present.copy(); marginal=[]
    for name,valid in raw_rules:
        v=frame[name]
        marginal.append({'variable':name,'denominator':int(joined.sum()),
                         'raw_missing':int((joined & v.isna()).sum()),
                         'invalid_or_zero_weight':int((joined & v.notna() & ~valid).sum()),
                         'invalid_raw_values':{str(k):int(n) for k,n in
                                               v[joined & v.notna() & ~valid].value_counts().items()},
                         'unusable_total':int((joined & ~valid).sum())})
        before=int(retained.sum()); retained &=valid
        flow.append({'step':name,'remaining':int(retained.sum()),'excluded':before-int(retained.sum())})
    return frame, joined, retained, flow, marginal, weight


def compare_svy(frame, retained, formula, weight, reference):
    y,x=patsy.dmatrices(formula,frame.loc[retained],return_type='dataframe',NA_action='raise')
    names=list(x.columns)
    # Keep every positive-weight record in the design; zero-filled fields outside
    # the domain are placeholders, explicitly excluded using where=domain.
    full=frame.loc[frame[weight].gt(0),['SEQN','SDMVSTRA','SDMVPSU',weight]].copy()
    full['domain']=retained.loc[full.index]
    full['outcome']=0.
    full.loc[y.index,'outcome']=np.asarray(y).ravel()
    safe_names=['x'+str(i) for i in range(len(names))]
    for name,safe in zip(names,safe_names):
        full[safe]=0.; full.loc[x.index,safe]=x[name]
    data=pl.DataFrame({c:full[c].to_numpy() for c in full})
    sample=svy.Sample(data,svy.Design(stratum='SDMVSTRA',psu='SDMVPSU',wgt=weight,wr=True))
    model=sample.glm.fit(y='outcome',x=safe_names,intercept=False,family='gaussian',
                         where=svy.col('domain')==True)
    table=model.to_polars().to_dicts()
    mapped={row['term']:row for row in table}
    rows=[]
    for name,safe in zip(names,safe_names):
        row=mapped[safe]; a=reference['coefficients'][name]
        rows.append({'term':name,'cycle001_estimate':a['estimate'],'svy_estimate':float(row['estimate']),
                     'cycle001_se':a['se'],'svy_se':float(row['std_err']),
                     'se_ratio':float(row['std_err']/a['se']),
                     'svy_df':float(row['df']), 'cycle001_df':reference['df_design'],
                     'svy_ci_low':float(row['conf_low']), 'svy_ci_high':float(row['conf_high']),
                     'svy_p_with_cycle001_df':float(2*stats.t.sf(abs(row['estimate']/row['std_err']),reference['df_design'])),
                     'svy_p':float(row['p_value']) if np.isfinite(row['p_value']) else None,
                     'cycle001_p':a['p_value']})
    return {'full_design_n':len(full),'matrix_rank':int(np.linalg.matrix_rank(x)),
            'matrix_columns':len(names),'terms':rows,
            'max_abs_beta_difference':max(abs(r['svy_estimate']-r['cycle001_estimate']) for r in rows),
            'max_relative_se_difference':max(abs(r['se_ratio']-1) for r in rows)}


def main():
    tables={n:old.read_xpt(n) for n in ['DEMO_L','DR1TOT_L','SLQ_L','PAQ_L','DPQ_L','DSQTOT_L']}
    ref=json.loads((PREVIOUS/'results.json').read_text())
    report={'date':'2026-09-09','versions':{n:importlib.metadata.version(n) for n in ['svy','numpy','pandas','polars','statsmodels','scipy']},'models':{},'diagnostic_groups':'not_assessed'}
    for h in TABLES:
        frame,joined,retained,flow,marginal,weight=prepare(h,tables)
        assert retained.sum()==ref['models'][h]['n'],h
        # Verify the participant set against the cycle001 formula, not only N.
        rerun=old.survey_wls(ref['models'][h]['formula'],frame.loc[joined],weight)
        assert set(rerun['used_index'])==set(frame.index[retained]),h
        for term,a in ref['models'][h]['coefficients'].items():
            np.testing.assert_allclose(rerun['coefficients'][term]['estimate'],a['estimate'],atol=1e-9,rtol=1e-9)
        cells=[]
        for (s,p),block in frame.loc[frame[weight].gt(0)].groupby(['SDMVSTRA','SDMVPSU']):
            ids=block.index
            cells.append({'stratum':int(s),'psu':int(p),'positive_weight_n':len(block),
                          'joined_adults':int(joined.loc[ids].sum()),'retained':int(retained.loc[ids].sum())})
        comp=compare_svy(frame,retained,ref['models'][h]['formula'],weight,ref['models'][h])
        report['models'][h]={'n_joined':int(joined.sum()),'n_retained':int(retained.sum()),
          'retention':float(retained.sum()/joined.sum()),'weight':weight,'flow':flow,'marginal':marginal,
          'age18_19_joined':int((joined & frame.RIDAGEYR.lt(20)).sum()),
          'age18_19_missing_education':int((joined & frame.RIDAGEYR.lt(20)&frame.DMDEDUC2.isna()).sum()),
          'weight_summary':weight_summary(frame.loc[retained,weight]),
          'weight_summary_joined_positive':weight_summary(frame.loc[joined & frame[weight].gt(0),weight]),
          'psu_cells':cells,'variance_comparison':comp}
        if h=='H3':
            r=report['models'][h]
            r['supplement_categories']={
                'use_yes_mag_missing':int((retained & frame.DSD010.eq(1)&frame.DSQTMAGN.isna()).sum()),
                'use_no_mag_missing':int((retained & frame.DSD010.eq(2)&frame.DSQTMAGN.isna()).sum()),
                'use_no_mag_reported':int((retained & frame.DSD010.eq(2)&frame.DSQTMAGN.notna()).sum()),
                'mag_reported':int((retained & frame.DSQTMAGN.notna()).sum())}
        print(h,report['models'][h]['n_retained'],report['models'][h]['weight_summary'],comp['max_abs_beta_difference'],comp['max_relative_se_difference'],flush=True)
    # Cross-check tiny SAS floats and codebook totals without changing raw data.
    ds=tables['DSQTOT_L']; raw=pd.read_sas(old.DATA/'DSQTOT_L.xpt',format='xport')
    report['codebook_checks']={'DSD010_yes':int(ds.DSD010.eq(1).sum()),'DSD010_no':int(ds.DSD010.eq(2).sum()),
       'DSQTMAGN_present':int(ds.DSQTMAGN.notna().sum()),'WTDRD1_zero':int(ds.WTDRD1.eq(0).sum()),
       'WTDRD1_raw_tiny_nonzero':int(((raw.WTDRD1.abs()<old.ZERO_THRESHOLD)&raw.WTDRD1.ne(0)).sum())}
    assert report['codebook_checks']=={'DSD010_yes':3762,'DSD010_no':2969,'DSQTMAGN_present':1613,'WTDRD1_zero':2106,'WTDRD1_raw_tiny_nonzero':2106}
    report['input_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(old.DATA.glob('*.xpt')) if p.stem in tables}
    assert report['input_sha256']==ref['input_sha256']
    primary={'H1':['CAFF100','CAFF_X_AGE'], 'H2':['C(SLEEP_CAT)[T.short]','C(SLEEP_CAT)[T.long]','SED_HOURS'],
             'H3':['DIET_MAG100','SUPP_MAG100','SUPP_MAG_UNQUANT']}
    report['primary_df_sensitivity']=[]
    for h,terms in primary.items():
        for row in report['models'][h]['variance_comparison']['terms']:
            if row['term'] in terms: report['primary_df_sensitivity'].append({'model':h,**row})
    for field,out_field in [('svy_p','q_svy_default'),('svy_p_with_cycle001_df','q_design_df15')]:
        adjusted=multipletests([r[field] for r in report['primary_df_sensitivity']],method='fdr_bh')[1]
        for row,q in zip(report['primary_df_sensitivity'],adjusted): row[out_field]=float(q)
    report['df_convention']='cycle001: PSU minus strata = 15; svy 0.28.0 default: max(1, design_df - (k - 1)) = 1'
    report['svy_source_sha256']=hashlib.sha256((Path(svy.__file__).parent/'regression/base.py').read_bytes()).hexdigest()
    report['provenance_sha256']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),OUT/'protocol.md',PREVIOUS/'run_analysis.py',PREVIOUS/'results.json',ROOT/'Pipfile.lock']}
    (OUT/'results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    make_figures(report)


def make_figures(report):
    (OUT/'figures').mkdir(exist_ok=True)
    models=report['models']; labels=list(models)
    fig,ax=plt.subplots(figsize=(9,4.8))
    remaining=[models[h]['n_retained'] for h in labels]; lost=[models[h]['n_joined']-models[h]['n_retained'] for h in labels]
    ax.barh(labels,remaining,label='Casos completos',color='#087e8b')
    ax.barh(labels,lost,left=remaining,label='Excluídos após junções',color='#c4cbd0')
    for i,h in enumerate(labels):
        totals=f"{remaining[i]:,} / {models[h]['n_joined']:,}".replace(',','.')
        percent=f"{models[h]['retention']:.1%}".replace('.',',')
        ax.text(70,i,f"{totals} ({percent})",va='center',color='white')
    ax.set(xlabel='Participantes (contagens não ponderadas)',title='NHANES 2021–2023: retenção após junções de adultos')
    ax.legend(loc='lower right');fig.tight_layout();fig.savefig(OUT/'figures/selection.png',dpi=180);plt.close(fig)
    fig,ax=plt.subplots(figsize=(9,4.8)); x=np.arange(3)
    ax.bar(x-.18,remaining,.36,label='N observado',color='#087e8b')
    kish=[models[h]['weight_summary']['kish_n'] for h in labels]
    ax.bar(x+.18,kish,.36,label='Kish: somente desigualdade dos pesos',color='#e98436')
    ax.set(xticks=x,xticklabels=labels,ylabel='Número de participantes',title='Pesos analíticos: WTDRD1 (H1/H3), WTMEC2YR (H2)\nKish não incorpora estratificação, clusters ou o desfecho')
    ax.set_ylim(0,max(remaining)*1.28)
    ax.legend();fig.tight_layout();fig.savefig(OUT/'figures/weights.png',dpi=180);plt.close(fig)


if __name__=='__main__': main()
