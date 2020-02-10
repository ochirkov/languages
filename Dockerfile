FROM python:3.7.5-alpine3.10


ENV PIP_NO_CACHE_DIR=true
ENV FLASK_APP=app.py

WORKDIR /app

RUN addgroup \
    -g 1000  \
    -S languagewire && \
    adduser --gecos 'languagewire' \
    -D -u 1000  \
    -G languagewire languagewire

COPY requirements.txt ./
RUN pip install -r requirements.txt

USER languagewire

COPY . /app

CMD gunicorn -w 2 -b 0.0.0.0:5000 --access-logfile - wsgi
