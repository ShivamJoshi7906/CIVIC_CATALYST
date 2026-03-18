#!/usr/bin/env bash
# Render build script
set -o errexit

pip install --upgrade pip

# Install with relaxed dependency checking to handle django-mongodb-backend conflict
pip install -r requirements.txt --no-deps
pip install -r requirements.txt --ignore-installed 2>/dev/null || true

python manage.py collectstatic --no-input
