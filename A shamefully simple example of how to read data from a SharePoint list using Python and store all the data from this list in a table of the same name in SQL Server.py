from office365.sharepoint.client_context import ClientContext # pip install Office365-REST-Python-Client
from office365.runtime.auth.client_credential import ClientCredential
import pyodbc # pip install pyodbc
import pandas as pd # pip install pandas

# Configurações do SharePoint
SHAREPOINT_SITE_URL = "https://seusite.sharepoint.com"
CLIENT_ID = "seu-client-id"
CLIENT_SECRET = "seu-client-secret"
LIST_NAME = "NomeDaLista"

# Configurações do SQL Server
SQL_SERVER = "seu-servidor.database.windows.net"
SQL_DATABASE = "seu-banco"
SQL_USERNAME = "seu-usuario"
SQL_PASSWORD = "sua-senha"
SQL_TABLE = LIST_NAME  # Criando a tabela com o mesmo nome da lista

# Autenticação no SharePoint
ctx = ClientContext(SHAREPOINT_SITE_URL).with_credentials(ClientCredential(CLIENT_ID, CLIENT_SECRET))
list_obj = ctx.web.lists.get_by_title(LIST_NAME)
items = list_obj.items.get().execute_query()

# Convertendo os dados para um DataFrame
data = [{prop: getattr(item, prop, None) for prop in item.properties} for item in items]
df = pd.DataFrame(data)

# Conectando ao SQL Server
conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SQL_SERVER};DATABASE={SQL_DATABASE};UID={SQL_USERNAME};PWD={SQL_PASSWORD}"
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Criando a tabela se não existir
columns = ", ".join(f"[{col}] NVARCHAR(MAX)" for col in df.columns)
create_table_query = f"IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{SQL_TABLE}') CREATE TABLE {SQL_TABLE} ({columns})"
cursor.execute(create_table_query)

# Inserindo os dados no SQL Server
for _, row in df.iterrows():
    placeholders = ", ".join("?" * len(row))
    insert_query = f"INSERT INTO {SQL_TABLE} VALUES ({placeholders})"
    cursor.execute(insert_query, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("Dados inseridos com sucesso no SQL Server!")
