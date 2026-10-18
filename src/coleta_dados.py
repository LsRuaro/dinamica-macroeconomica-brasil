import os
import requests
import pandas as pd

os.makedirs('dados', exist_ok=True)

SIDRA_API = 'http://api.sidra.ibge.gov.br/values'

# Configurações das tabelas do SIDRA/IBGE:
# - Tabela 1846: Preços correntes (Nominal)
# - Tabela 6612: Valores encadeados a preços de 1995 (Real)
tabelas = {
    'nominal': {
        'url': f'{SIDRA_API}/t/1846/n1/all/p/all/c11255/all',
        'arquivo_saida': 'dados/despesas_trimestrais_setores_nominal.csv'
    },
    'real': {
        'url': f'{SIDRA_API}/t/6612/n1/all/p/all/c11255/all',
        'arquivo_saida': 'dados/despesas_trimestrais_setores_real.csv'
    }
}

for tipo, config in tabelas.items():
    r = requests.get(config['url'])
    r.raise_for_status()

    dados = pd.DataFrame(r.json())

    # Ajusta o cabeçalho
    dados.columns = dados.iloc[0]
    dados = dados.drop(0)

    # Remove os dados de 2026
    dados = dados[~dados['Trimestre'].str.contains('2026', na=False)]

    dados.to_csv(config['arquivo_saida'], encoding='UTF-8-sig', sep=';', index=False)