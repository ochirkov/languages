FROM python:3.7.5-alpine3.10


ENV PIP_NO_CACHE_DIR=true
ENV FLASK_APP=app.py

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt && \
    rm -f ./requirements.txt

COPY app.py wsgi.py /app/

CMD gunicorn -w 2 -b 0.0.0.0:5000 --access-logfile - wsgi
