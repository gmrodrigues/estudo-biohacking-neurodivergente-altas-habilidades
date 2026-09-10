# Acesso às fontes a partir deste ambiente

Atualização de 2026-09-10: a [triagem de adequação](SOURCE_FIT_AUDIT.md) registra
ABCD 7.0/NBDC, requisitos HBN e campos públicos UK Biobank. A FAQ ABCD proíbe
inserir dados em IA generativa: acesso individual não autoriza sua leitura por
este assistente. Aqui, trabalhar com documentação pública e código sem microdados;
a execução com dados exige fluxo compatível com o acordo.
Esclarecimento operacional: download por ferramenta e execução local de script
podem ser orquestrados sem inserir dados no modelo. Não é uma proibição geral
de automação. O [fluxo ABCD](ABCD_LOCAL_WORKFLOW.md) mantém arquivos e relatórios
locais e evita retorno de registros à conversa, condicionado ao acesso legítimo.
Fonte: https://docs.abcdstudy.org/latest/info/faq.html
As matrizes abaixo preservam a inspeção histórica de 07/09, não verificam o acesso
individual atual.

Esta matriz documenta a capacidade operacional de acessar as fontes catalogadas
a partir do workspace atual. “Direto” significa que dados públicos podem ser
consultados por página, API ou download sem usar uma conta pessoal do pesquisador.

O acesso direto não garante que todo o acervo da fonte seja aberto. Também pode
haver bloqueios temporários de rede, limites de API, termos de uso, arquivos muito
grandes ou mudanças no serviço. A situação abaixo foi verificada em 2026-09-07.

## Acesso direto

| Fonte | Página pública | API/download | O que pode ser feito daqui | Observações |
|---|---:|---:|---|---|
| NHANES | Sim | Sim | Baixar e analisar questionários, exames, dieta, suplementos e atividade física | Arquivos XPT; análises populacionais precisam usar o desenho amostral |
| DSLD | Sim | Sim | Consultar produtos, ingredientes, doses, marcas e rótulos | O rótulo não comprova o conteúdo real do produto |
| DSID | Sim | Sim | Obter tabelas e relatórios de conteúdo analisado | Não valida individualmente toda marca ou unidade |
| ClinicalTrials.gov | Sim | Sim | Pesquisar e baixar protocolos, intervenções, desfechos e resultados | Ausência de resultados não significa ausência de estudo |
| PubChem | Sim | Sim | Consultar compostos, bioatividade, toxicologia e referências | Evidência mecanística não demonstra eficácia clínica |
| openFDA CAERS | Sim | Sim | Baixar e analisar eventos adversos associados a suplementos | Notificações detectam sinais; não demonstram causalidade ou incidência |
| OpenNeuro | Sim | Sim | Localizar e baixar conjuntos públicos de neuroimagem e neurofisiologia | Conferir licença e documentação de cada conjunto |
| NIH ODS Fact Sheets | Sim | Parcial | Consultar sínteses de eficácia, segurança e interações | São revisões e referências, não microdados individuais |
| PhysioNet | Sim | Parcial | Acessar conjuntos explicitamente marcados como abertos | Conjuntos credenciados exigem conta, treinamento e termo de uso |

## Acesso público com maior atrito técnico

| Fonte | O que pode ser feito daqui | Limitação prática |
|---|---|---|
| DATASUS | Consultar TABNET e baixar microdados públicos | Downloads e formatos DBC/DBF podem exigir conversão e tratamento específico |
| Anvisa / Nutrivigilância | Consultar alertas, regulamentos, boletins e painéis públicos | Nem todo dado está disponível como tabela bruta ou API estável |
| Open Humans | Acessar somente dados que membros publicaram explicitamente | Dados privados exigem consentimento, autorização e configuração de projeto |

## Dependência de credenciais ou aprovação

| Fonte | Parte diretamente acessível | O que exige ação do pesquisador |
|---|---|---|
| NIMH Data Archive / ABCD | Catálogo, metadados, dicionários e documentação pública | Dados individuais exigem conta qualificada e aprovação do NDA |
| All of Us | Data Browser, snapshots e estatísticas agregadas | Dados individuais exigem Researcher Workbench, identidade, treinamento e instituição elegível |
| NSRR | Catálogo, documentação e descoberta de conjuntos | Download normalmente exige cadastro, solicitação e aceite do acordo da coorte |
| PhysioNet credenciado | Descrição e documentação pública | Dados restritos exigem conta, treinamento ético e termo de uso |
| Open Humans privado | Perfis e arquivos explicitamente públicos | Dados de membros exigem opt-in e autorização para o projeto |

Credenciais pessoais, aceite de termos e aprovações institucionais não devem ser
contornados. Quando uma fonte exigir autenticação, o pesquisador deve obter o
acesso legítimo; depois, os arquivos autorizados podem ser colocados no workspace
para preparação e análise, respeitando o acordo aplicável.

## Sequência recomendada para pesquisa de suplementação

1. Usar NHANES para exposição populacional, exames e associações observacionais.
2. Usar ClinicalTrials.gov para localizar evidência experimental e seus protocolos.
3. Usar DSLD e DSID para caracterizar formulação declarada e conteúdo analisado.
4. Usar PubChem para normalizar substâncias e explorar mecanismo/toxicologia.
5. Usar openFDA CAERS e Anvisa para procurar sinais de segurança.
6. Somente então desenhar uma análise integrada ou um protocolo N-of-1.

Essa sequência organiza evidências, mas não transforma associação em causalidade
nem substitui avaliação clínica de dose, deficiência, contraindicação ou interação
com medicamentos.
