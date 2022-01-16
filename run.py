import os
import json
from quart import Quart, request

app = Quart(__name__)


@app.route("/")
async def main():
    return json.dumps(dict(request.headers))


app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000))
