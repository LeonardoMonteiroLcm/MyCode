import pandas as pd # pip install pandas
from office365.sharepoint.client_context import ClientContext # pip install office365-rest-python-client
from office365.runtime.auth.client_credential import ClientCredential

def upload_excel_to_sharepoint(excel_file, site_url, client_id, client_secret):
    # Autenticando no SharePoint
    ctx = ClientContext(site_url).with_credentials(ClientCredential(client_id, client_secret))
    
    # Lendo o arquivo Excel
    xls = pd.ExcelFile(excel_file)
    
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        
        # Criando a lista no SharePoint
        list_creation_info = {
            'Title': sheet_name,
            'BaseTemplate': 100  # Template para listas customizadas
        }
        sp_list = ctx.web.lists.add(list_creation_info)
        ctx.execute_query()
        
        # Criando colunas na lista com base nos nomes das colunas do DataFrame Excel
        for col_name in df.columns:
            field_schema = f'<Field DisplayName="{col_name}" Type="Text" />'
            sp_list.fields.add_field_as_xml(field_schema)
            ctx.execute_query()
        
        # Adicionando os dados do DataFrame Excel na lista
        for _, row in df.iterrows():
            item_properties = {col: str(row[col]) for col in df.columns}
            sp_list.add_item(item_properties)
            ctx.execute_query()
    
    print("Dados importados do Excel com sucesso!")

# Exemplo de uso
upload_excel_to_sharepoint("dados.xlsx",
                           "https://seusite.sharepoint.com/sites/seusite",
                           "seu_client_id",
                           "seu_client_secret")