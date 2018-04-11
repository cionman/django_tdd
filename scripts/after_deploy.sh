#!/usr/bin/env bash
/root/.pyenv/versions/django_tdd/bin/pip install --upgrade pip
/root/.pyenv/versions/django_tdd/bin/pip install -r /home/django-tdd/requirements/requirements-prod.txt
pkill -HUP gunicorn