FROM python:3.6-alpine

WORKDIR /home/facerecdb

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

COPY . ./
RUN chmod a+x boot.sh

ENV FLASK_APP facerecdb.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
