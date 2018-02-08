#!/bin/sh
# this script is used to boot a Docker container

export FLASK_APP=facerecdb.py
flask db upgrade
python3 generate_index.py
exec gunicorn -b :5000 --access-logfile - --error-logfile - facerecdb:app
