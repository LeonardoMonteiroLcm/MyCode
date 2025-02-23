from shareplum import Site # pip install shareplum
from shareplum import Office365
from shareplum.site import Version

# Configurações
sharepoint_url = "https://seu-dominio.sharepoint.com"
site_url = "/sites/seu-site"
username = "seu-login@seu-dominio.com"
password = "sua-senha"
list_name = "Clientes"

# Autenticação no SharePoint Online
authcookie = Office365(sharepoint_url, username=username, password=password).GetCookies()
site = Site(site_url, version=Version.v365, authcookie=authcookie)

# Criar uma nova lista
list_data = {
    "Title": list_name,
    "BaseTemplate": 100,  # Template de lista personalizada
    "Description": "Lista de clientes com ID, Nome, Endereço e CPF"
}

# Adicionar campos à lista
fields = [
    {"FieldType": "Text", "DisplayName": "ID", "InternalName": "ID", "Required": True},
    {"FieldType": "Text", "DisplayName": "Nome", "InternalName": "Nome", "Required": True},
    {"FieldType": "Text", "DisplayName": "Endereco", "InternalName": "Endereco", "Required": False},
    {"FieldType": "Text", "DisplayName": "CPF", "InternalName": "CPF", "Required": False}
]

# Criar a lista
new_list = site.AddList(list_data)

# Adicionar campos à lista
for field in fields:
    new_list.AddField(field)

print(f"Lista '{list_name}' criada com sucesso!")