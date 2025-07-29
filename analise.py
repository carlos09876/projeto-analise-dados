
import pandas as pd

# Exemplo de DataFrame fictício
dados = {
    'Produto': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Vendas': [100, 150, 200, 120, 130, 180]
}

df = pd.DataFrame(dados)

# Agrupamento por produto e soma das vendas
vendas_totais = df.groupby('Produto')['Vendas'].sum().reset_index()

# Exibir resultado
print("Total de vendas por produto:")
print(vendas_totais)

# Salvar em CSV
vendas_totais.to_csv('vendas_totais.csv', index=False)
