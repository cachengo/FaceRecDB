FROM python:3.6

WORKDIR /home/facerecdb

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn pymysql

COPY . ./
RUN chmod a+x boot.sh

ENV FLASK_APP facerecdb.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
