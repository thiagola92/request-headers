import os
import json
from quart import Quart, request
from request_headers.mongo import insert_headers
from request_headers.headers import clean_headers

app = Quart(__name__)


@app.route("/")
async def main():
    headers = dict(request.headers)

    clean_headers(headers)
    insert_headers(headers)

    return json.dumps(headers)


app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000))
