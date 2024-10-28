from flask import Flask
from flask_bootstrap import Bootstrap4
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json
from dotenv import load_dotenv 

load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    bootstrap = Bootstrap4(app)

    app.config['URL'] = 'https://drive.google.com/file/d/1GnjnNrRUGHJ9UtEOQO-sUB69KemfUGl4/view?usp=sharing'

    # Escopos para autenticação
    scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    
    # Carregar credenciais a partir da variável de ambiente
    creds_json = os.environ.get('GOOGLE_CREDENTIALS_JSON')
    creds_dict = json.loads(creds_json)
    
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    
    app.config['GOOGLE_CLIENT'] = client  # Armazena o cliente gspread na configuração do app

    # Importar rotas
    from .routes import index  # Adiciona as funções das rotas
    app.add_url_rule('/', view_func=index, methods=['GET', 'POST'])  # Define a rota diretamente

    return app