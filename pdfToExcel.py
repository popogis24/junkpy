import tabula
import pandas as pd

# Define o caminho do arquivo PDF de entrada e do arquivo Excel de saída
pdf_file_path = fr"C:\Users\anderson.souza\Documents\teste_py\IPF_CadastroGeral_21Ago23.pdf"
excel_file_path = fr"C:\Users\anderson.souza\Documents\teste_py\testepy.xlsx"

# Extrai as tabelas do PDF e coloca em uma lista de DataFrames
tables = tabula.read_pdf(pdf_file_path, pages="all", multiple_tables=True)

# Assume que a tabela desejada está na primeira posição da lista (pode ser ajustado conforme necessário)
table_df = tables[0]

# Converte a tabela em um DataFrame pandas
df = pd.DataFrame(table_df)

# Exporta o DataFrame para um arquivo Excel
df.to_excel(excel_file_path, index=False, engine="openpyxl")

print("Tabela exportada com sucesso para Excel.")
