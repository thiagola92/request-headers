import json
import os
import sys

from quart import Quart, request

from request_headers.headers import clean_headers
from request_headers.mongo import insert_headers

app = Quart(__name__)


@app.route("/")
async def main():
    headers = dict(request.headers)

    clean_headers(headers)
    insert_headers(headers)

    return json.dumps(headers)


@app.route("/exit")
async def exit():
    sys.exit(0)


app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000))
