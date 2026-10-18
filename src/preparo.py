import pandas as pd

# Componentes da demanda agregada
componentes_demanda_agregada = [
    'PIB a preços de mercado',
    'Despesa de consumo das famílias',
    'Despesa de consumo da administração pública',
    'Formação bruta de capital fixo',
    'Variação de estoque',
    'Exportação de bens e serviços',
    'Importação de bens e serviços (-)'
]

arquivos = {
    'nominal': {
        'entrada': 'dados/despesas_trimestrais_setores_nominal.csv',
        'saida': 'dados/despesas_anuais_nominal.csv'
    },
    'real': {
        'entrada': 'dados/despesas_trimestrais_setores_real.csv',
        'saida': 'dados/despesas_anuais_real.csv'
    }
}

for tipo, config in arquivos.items():
    despesas_trimestrais = pd.read_csv(config['entrada'], sep=';')

    # Extrai o ano do código do trimestre
    despesas_trimestrais['Ano'] = despesas_trimestrais['Trimestre (Código)'].astype(str).str[:4]

    # Filtra apenas os componentes da demanda agregada
    despesas_componentes = despesas_trimestrais[
        despesas_trimestrais['Setores e subsetores'].isin(componentes_demanda_agregada)
    ]

    # Agregação anual via pivot de tabela
    despesas_anuais = despesas_componentes.pivot_table(
        index='Ano',
        columns='Setores e subsetores',
        values='Valor',
        aggfunc='sum'
    )

    despesas_anuais.to_csv(config['saida'], encoding='UTF-8-sig', sep=';')