# Dinâmica Macroeconômica do Brasil

**Do PIB aos choques de demanda e oferta, com dados brasileiros**

Projeto de macroeconomia aplicada em Python. A ideia é medir o PIB brasileiro pela ótica da despesa, calibrar a oferta agregada com dados reais e simular choques de demanda e de oferta partindo da estrutura real da economia.

> **Status: em desenvolvimento.** A etapa 1 (contabilidade nacional) está concluída. O simulador e a curva de Phillips ainda não foram implementados.

## Status

| Etapa | Descrição | Situação |
|---|---|---|
| 1 | PIB pela ótica da despesa: participações e contribuições ao crescimento | Concluída |
| 2 | Curva de Phillips (oferta agregada de curto prazo) | A fazer |
| 3 | Simulador AD-AS com choques de gasto público e de oferta | A fazer |

## O que a etapa 1 faz

1. **Decompõe o PIB em C, I, G e X − M**, em valores correntes (1996–2025), e mostra a composição ao longo do tempo.
2. **Calcula a contribuição de cada componente à variação real do PIB**, em pontos percentuais, a partir de séries em volume.
3. **Valida os dados:** a soma dos componentes é comparada com o PIB publicado pelo IBGE.

O trabalho está no notebook [`notebooks/demanda_agregada.ipynb`](notebooks/demanda_agregada.ipynb).

## Conceitos

A identidade do PIB pela ótica da despesa é uma identidade contábil, e vale por definição:

```
Y = C + I + G + (X − M)
```

- **C:** despesa de consumo das famílias
- **I:** investimento = formação bruta de capital fixo (FBCF) + variação de estoque
- **G:** despesa de consumo da administração pública
- **X − M:** exportações líquidas de importações

A contribuição de um componente ao crescimento é a variação dele dividida pelo PIB do ano anterior:

```
contribuição_t = (componente_t − componente_t−1) / PIB_t−1 × 100        [p.p.]
```

A importação entra com sinal negativo. Uma contribuição positiva da importação significa que ela **caiu**, e isso é consequência da conjuntura, não uma causa do crescimento.

## Dados

Fonte: **IBGE, Contas Nacionais Trimestrais**, coletadas pela API do SIDRA.

| Tabela | Conteúdo | Uso |
|---|---|---|
| 1846 | Valores a preços correntes | Participações no PIB |
| 6612 | Valores encadeados a preços de 1995 | Contribuições ao crescimento |

- Período: 1996-2025. 2026 fica de fora por estar incompleto.
- Unidade: milhões de reais.

## Decisões metodológicas

- **Valores correntes e valores reais não se misturam.** A composição usa a série nominal. As contribuições usam a série real. Cada uma é comparada só dentro da própria base.
- **Não há variação de estoque na série real (6612).** Por isso, em volume, o investimento é representado apenas pela FBCF. A barra "Estoques e resíduo" do gráfico de contribuições reúne a variação de estoques e a não aditividade das séries encadeadas.
- **O volume anual é a soma dos quatro trimestres** de uma série encadeada.
- **G no IBGE é só consumo do governo** (salários e serviços). Investimentos públicos estão dentro da FBCF.
- **A leitura do gráfico é aritmética, não causal.** Mostra quanto cada componente respondeu pela variação do PIB, e não por que ele variou.

## Validação

A soma C + I + G + (X − M), em valores correntes, foi comparada com o PIB publicado pelo IBGE. A diferença máxima observada na série anual foi de R$ 4 milhões, atribuída a arredondamento (os componentes são publicados em milhões inteiros). A validação anual está no notebook.

## Estrutura do repositório

```
.
├── README.md
├── dados/                   # CSVs coletados e tabelas anuais
├── notebooks/
│   └── demanda_agregada.ipynb
└── src/
    ├── coleta_dados.py      # coleta via API do SIDRA
    └── preparo.py           # preparo das tabelas anuais
```

## Limitações

- O IBGE revisa a série histórica. Os resultados podem mudar entre coletas.
- A decomposição por componente não separa investimento público de privado.
- Os resultados são descritivos e não permitem concluir causalidade.

## Próximos passos

1. **Simulador AD-AS** com dois choques: corte do gasto público (demanda) e alta do preço do petróleo (oferta). Ponto de partida: a estrutura real de C, I, G e X − M. Parâmetros ajustáveis: propensão marginal a consumir, alíquota de impostos, propensão a importar e inclinação da oferta. Os resultados serão apresentados como "dadas estas hipóteses", e não como previsão.
2. **Curva de Phillips** (IPCA contra o hiato do produto, com expectativas de inflação) para calibrar a inclinação da oferta agregada de curto prazo.
