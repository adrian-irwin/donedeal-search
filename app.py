from flask import Flask, request

from donedeal_search import get_all_ads, get_body

app = Flask(__name__)


@app.route("/search", methods=["POST"])
def search():
    inputs = request.get_json()

    body = get_body(inputs)

    ads = get_all_ads(body)

    return ads
