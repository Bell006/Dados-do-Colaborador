# Coleta arquivos estáticos
python manage.py collectstatic --noinput

# Inicia o Gunicorn
gunicorn guia_ponto.wsgi:application --config gunicorn_config.py