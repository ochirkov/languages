# Merry Christmas 🎄
***
**Note that this code is TEST code.  
It is intended for testing basic deployment related tasks in an interview environment, and nothing other than that.**
***
A hello-world'ish Python3 Flask application that simply maps [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes to translations of 'Merry christmas' and serves it as JSON.

## Usage
Install dependencies with `pip3 install -r requirements.txt`.

```bash
# For development, run the application at port 5000 with:
python3 wsgi.py

# For production, run it using gunicorn with:
gunicorn -w <WORKERS> -b <HOST>:<PORT> wsgi

# To get access log printed to standed out, run with:
gunicorn -w <WORKERS> -b <HOST>:<PORT> --access-logfile - wsgi
```

Now you can find a bunch of nice translations at `localhost:<PORT>/lw/xmas/<TARGET_LANGUAGE>`.
```bash
curl localhost:<PORT>/lw/xmas/de
```

The supported language codes are: *cs, da, de, el, en, es, it, nl, pl, ru*



## Prepare gcloud
```bash
# Use login
gcloud config set project  technical-challenges
gcloud auth login

# or use auth.json
gcloud auth activate-service-account \
  --key-file=/Users/alex/auth.json
```

## Deploy
```bash
curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/v1.3.1/skaffold-linux-amd64 \
    && chmod +x skaffold \
    && sudo mv skaffold /usr/local/bin
```
skaffold deploy -p prepare
skaffold run -p languagewire


## Run query script
```bash

python3 query_script.py --ip <ingress-external-ip> --count 4  # For 4 requests per second
python3 query_script.py --ip <ingress-external-ip> --count 10  # For 10 requests per second
```