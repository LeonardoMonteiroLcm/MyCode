from office365.sharepoint.client_context import ClientContext # pip install Office365-REST-Python-Client
from office365.runtime.auth.client_credential import ClientCredential

# Configurações do SharePoint
site_url = "https://seu-dominio.sharepoint.com/sites/seu-site"
client_id = "SEU_CLIENT_ID"
client_secret = "SEU_CLIENT_SECRET"

# Autenticação
ctx = ClientContext(site_url).with_credentials(ClientCredential(client_id, client_secret))

# Nome da lista no SharePoint
list_title = "NomeDaLista"

# Obtendo os itens da lista
sp_list = ctx.web.lists.get_by_title(list_title)
items = sp_list.items.get().execute_query()

# Exibir os dados no console
for item in items:
    print(f"ID: {item.properties.get('ID')}, Título: {item.properties.get('Title')}")

