from flask import render_template, request, redirect, flash, current_app
from app.utils import add_to_google_sheet
from datetime import *

def index():
    bootstrap = current_app.extensions['bootstrap']
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        date = datetime.now().strftime('%d-%m-%Y %H:%M')

        if not email or not name:
            flash('Todos os campos são obrigatórios.', 'error')
            return render_template('index.html', bootstrap=bootstrap)

        # Adiciona os dados à planilha do Google Sheets
        add_to_google_sheet(current_app.config['GOOGLE_CLIENT'], email, name, date)

        # Redireciona para a URL do documento
        return redirect(current_app.config['URL']) 
    return render_template('index.html', bootstrap=bootstrap)