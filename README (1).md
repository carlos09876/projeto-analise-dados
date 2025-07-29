
# Projeto de Análise de Dados com Python

## 📄 Descrição
Este projeto realiza uma análise simples de vendas usando Python e Pandas.

---

## ▶️ Como executar

### Requisitos
- Python 3 instalado
- Permissão de execução no terminal

### Passo a passo:
1. Abra o terminal na pasta onde estão os arquivos
2. Dê permissão de execução ao arquivo:
   ```bash
   chmod +x executar.sh
   ```
3. Execute o shell script:
   ```bash
   ./executar.sh
   ```

---

## 📂 Estrutura do projeto
- `analise.py`: script principal em Python que lê dados fictícios e gera relatório CSV
- `executar.sh`: script para rodar automaticamente o Python
- `vendas_totais.csv`: saída com a soma de vendas por produto

---

## 💡 Explicação do código Python
O código cria um DataFrame com dados fictícios de vendas, agrupa por produto e salva os totais em um arquivo CSV.

```python
import pandas as pd

dados = {
    'Produto': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Vendas': [100, 150, 200, 120, 130, 180]
}

df = pd.DataFrame(dados)
vendas_totais = df.groupby('Produto')['Vendas'].sum().reset_index()
print(vendas_totais)
vendas_totais.to_csv('vendas_totais.csv', index=False)
```
