FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

WORKDIR /app

# Copier requirements et installer dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet (y compris la base SQLite)
COPY . .

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Appliquer les migrations (créer les tables)
RUN python manage.py migrate --noinput

EXPOSE 8000

CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
