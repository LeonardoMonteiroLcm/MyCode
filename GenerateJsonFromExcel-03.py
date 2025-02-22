import pandas as pd
import json

# Caminho para o arquivo Excel
excel_file_path = 'XPTO.xlsx'

# Caminho para o arquivo JSON
json_file_path = 'XPTO.json'

# Ler o arquivo Excel sem cabeçalho e definir os nomes das colunas manualmente
df = pd.read_excel(excel_file_path, 
                   sheet_name='XPTO1', 
                   header=None, 
                   skiprows=9, 
                   names=['id', 'number1', 'string1', 'string2', 'string3', 'string4', 'string5'])

# Converter colunas de data para strings
for col in df.columns:
    if pd.api.types.is_datetime64_any_dtype(df[col]):
        df[col] = df[col].dt.strftime('%Y-%m-%d %H:%M:%S')

# Converter o DataFrame para JSON
json_string = df.to_json(orient='records', indent=2)

# Escrever o JSON no arquivo json_file_path
with open(json_file_path, 'w', encoding='utf8') as json_file:
    json_file.write(json_string)

print('Arquivo JSON gerado com sucesso!')