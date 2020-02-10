"""
Small hello-world'ish Flask application with a hint of christmas.
"""
from flask import Flask, jsonify

MERRY_CHRISTMAS_MAP = {
    "cs": "Veselé vánoce",
    "da": "Glædelig jul",
    "de": "Fröhliche weihnachten",
    "el": "Καλά Χριστούγεννα",
    "en": "Merry christmas",
    "es": "Feliz navidad",
    "it": "Buon natale",
    "nl": "Vrolijk kerstfeest",
    "pl": "Wesołych świąt",
    "ru": "С pождеством",
}

app = Flask(__name__)
# Unsafe, but prettier for our tiny bundle of christmas
app.config["JSON_AS_ASCII"] = False


@app.route("/")
def healthcheck():
    """We use / as a simple healthcheck"""
    return ("Healthy!", 200)


@app.route("/lw/xmas/<target_language_code>")
def merry_christmas(target_language_code):
    """Return a JSON map, mapping ISO 639-1 codes to corresponding translations."""
    lowercased_code = target_language_code.lower()
    if lowercased_code not in MERRY_CHRISTMAS_MAP:
        return ("This language code is not yet supported!", 501)

    return jsonify(MERRY_CHRISTMAS_MAP[lowercased_code])
