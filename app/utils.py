import gspread
import json
import os
from oauth2client.service_account import ServiceAccountCredentials

# Configura as credenciais
def get_google_sheets_service():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Carrega as credenciais da variável de ambiente
    creds_json = os.getenv('GOOGLE_CREDENTIALS_JSON')
    
    # Verifica se as credenciais foram carregadas
    if creds_json is None:
        raise ValueError("As credenciais do Google não estão definidas na variável de ambiente 'GOOGLE_CREDENTIALS_JSON'.")

    # Converte a string JSON em um dicionário
    creds_dict = json.loads(creds_json)
    
    # Cria as credenciais a partir do dicionário
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    
    # Autentica o cliente
    client = gspread.authorize(creds)
    return client

# Adiciona dados à planilha
def add_to_google_sheet(client, email, name, date):
    sheet = client.open("Acessos").sheet1  
    sheet.append_row([email, name, date])