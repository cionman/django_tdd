#!/usr/bin/env bash
/root/.pyenv/versions/django_tdd/bin/pip install --upgrade pip
/root/.pyenv/versions/django_tdd/bin/pip install -r /home/django-tdd/requirements/requirements-prod.txt
export DJANGO_SETTINGS_MODULE="conf.settings.production"
/root/.pyenv/versions/django_tdd/bin/python /home/django-tdd/manage.py migrate
pkill -HUP gunicorn