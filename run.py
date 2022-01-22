import os
import json
from request_headers.mongo import insert_headers
from quart import Quart, request

app = Quart(__name__)


@app.route("/")
async def main():
    insert_headers(dict(request.headers))
    return json.dumps(dict(request.headers))


app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000))
