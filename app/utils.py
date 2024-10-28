import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configura as credenciais
def get_google_sheets_service():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    return client

# Adiciona dados à planilha
def add_to_google_sheet(client, email, name):
    sheet = client.open("Acessos").sheet1  
    sheet.append_row([email, name]) 