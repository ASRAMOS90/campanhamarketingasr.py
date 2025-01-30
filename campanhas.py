# marketinganualempresax
Codigo criado para calcular resultado de campanha de marketing de uma determinada empresa. Codigo leva em consideração todas as campanhas de marketing realizada, qual foi seu retorno obtido e qual foi considerada a melhor campanha. 

import pandas as pd

dados = [
    {'campanha': 'Campanha A', 'gasto': 15000, 'retorno': 30000},
    {'campanha': 'Campanha B', 'gasto': 10000, 'retorno': 22000},
    {'campanha': 'Campanha C', 'gasto': 12000, 'retorno': 25000},
    {'campanha': 'Campanha D', 'gasto': 18000, 'retorno': 35000},
    {'campanha': 'Campanha E', 'gasto': 14000, 'retorno': 28000},
]

df = pd.DataFrame(dados)

df['roi'] = (df['retorno'] - df['gasto']) / df['gasto'] * 100  # ROI em porcentagem

total_gasto = df['gasto'].sum()
total_retorno = df['retorno'].sum()

roi_anual = (total_retorno - total_gasto) / total_gasto * 100

print("Resultados de Campanhas de Marketing Anuais:")
print(df)
print("\nTotal Gasto: R$", total_gasto)
print("Total Retorno: R$", total_retorno)
print(f"ROI Anual: {roi_anual:.2f}%")

melhor_campanha = df.loc[df['roi'].idxmax()]
print("\nMelhor Campanha:", melhor_campanha['campanha'])
