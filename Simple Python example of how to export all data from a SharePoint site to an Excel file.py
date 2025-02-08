import pandas as pd # pip install pandas
from office365.sharepoint.client_context import ClientContext # pip install office365-rest-python-client
from office365.runtime.auth.client_credential import ClientCredential

# Configurações do SharePoint
site_url = "https://seu_site.sharepoint.com/sites/seu_site"
client_id = "SEU_CLIENT_ID"
client_secret = "SEU_CLIENT_SECRET"

# Configurações do Excel
output_file = "sharepoint_lists.xlsx"

def upload_sharepoint_to_excel(site_url, client_id, client_secret, output_file):
    # Conectar ao SharePoint
    ctx = ClientContext(site_url).with_credentials(ClientCredential(client_id, client_secret))
    web = ctx.web
    ctx.load(web)
    ctx.execute_query()

    # Obter todas as listas do SharePoint
    lists = web.lists
    ctx.load(lists)
    ctx.execute_query()

    # Criar um dicionário para armazenar os dataframes de cada lista
    sheets = {}

    # Iterar sobre as listas e coletar os dados
    for sp_list in lists:
        if not sp_list.hidden: # Ignorar listas ocultas
            list_name = sp_list.title
            items = sp_list.items
            ctx.load(items)
            ctx.execute_query()
        
            data = []
            for item in items:
                data.append(item.properties) # Coletar os dados dos itens da lista
        
            if data:
                df = pd.DataFrame(data)
                sheets[list_name] = df

    # Exportar para um arquivo Excel
    with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
        for sheet_name, df in sheets.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Exportação concluída! Arquivo salvo como {output_file}")

# Exemplo de uso
upload_sharepoint_to_excel(site_url,
                           client_id,
                           client_secret,
                           output_file)