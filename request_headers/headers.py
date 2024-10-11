import hashlib
import logging

from json import dumps
from pathlib import Path
from datetime import datetime, timezone

from starlette.requests import Request


def clean_headers(headers) -> dict:
    """
    Remove non-standard fields.

    Standard: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
    """

    # Quart fields
    # headers.pop("Remote-Addr", None)

    return headers


def get_headers_digest(headers) -> str:
    headers_bytes = bytes(str(headers), encoding="utf8")
    md5 = hashlib.md5()
    md5.update(headers_bytes)

    return md5.hexdigest()


def save_headers(request: Request) -> dict:
    headers = dict(request.headers)
    endpoint = request.scope.get("path")
    headers = clean_headers(headers)
    headers_digest = get_headers_digest(headers)
    path = Path(f"data/{headers_digest}.json")

    if path.exists():
        logging.info(f"Headers to '{endpoint}' ignored")
        return headers

    path.write_text(
        dumps(
            {
                "headers": headers,
                "endpoint": endpoint,
                "created": str(datetime.now(tz=timezone.utc)),
            },
            indent=2,
        )
    )

    return headers
