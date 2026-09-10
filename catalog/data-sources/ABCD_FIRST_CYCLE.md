# Primeiro ciclo ABCD: capacidade contínua, perfil e trajetória

Este é o primeiro ciclo analítico planejado após a fundação de dados. Não é uma
análise de suplementos e não pressupõe que alta capacidade seja um diagnóstico.

## Pergunta

Entre jovens com medidas repetidas, padrões de sono e atividade em uma onda
antecedem mudança em função executiva na onda posterior? A associação difere ao
longo do contínuo de capacidade e por medidas independentes de TDAH/autismo?

## Construção analítica

```text
capacidade contínua = f(raciocínio, memória, linguagem, função executiva,
                        desempenho acadêmico)

desfecho(t+1) = função_executiva(t+1)
exposição(t)  = sono regular ou atividade física documentada
estratos      = capacidade contínua; TDAH e autismo medidos separadamente
```

P95/P98/P99 são cortes secundários de sensibilidade. O estimando principal usa
o contínuo e não chama a faixa superior de grupo clínico de “superdotado”.

## Sequência

1. Manifestar release, estruturas, ondas e hashes disponíveis sob acesso válido.
2. Executar POC-01 a POC-03 da fundação analítica.
3. Congelar uma regra de índice de capacidade e verificar cobertura/invariância
   apropriada à idade e à onda.
4. Executar POC-04 com um hábito e um desfecho; incluir resultado nulo.
5. Só então avaliar perfis latentes, interações e comparação com HBN.

## Ajuste mínimo e riscos

Registrar idade, sexo registrado, centro, contexto socioeconômico, onda, nível
prévio do desfecho, medicação/tratamento quando medido e perdas. O ajuste não
elimina confundimento não observado. Sono, alimentação e atividade podem ter
janelas e informantes distintos; variáveis incompatíveis permanecem separadas.

## Critérios de parada

- Não há ligação legítima participante-onda: parar POC longitudinal.
- Índice de capacidade depende de uma única medida ou é instável: manter apenas
  medidas separadas; não criar perfil alto.
- Diagnóstico/sintoma não tem instrumento ou informante documentado: não formar
  estrato de condição.
- Retenção ou sobreposição temporal não permite `t → t+1`: reclassificar a
  pergunta como transversal ou `needs_data`.

## Relação com outras fontes

HBN replica heterogeneidade de perfil quando seus termos e cobertura permitirem.
UK Biobank responde a exposições adultas, suplementos e biomarcadores em outro
contexto. NHANES continua como referência de quantificação nutricional. Nenhuma
dessas fontes é unida a ABCD por indivíduo ou por escore de perfil.
