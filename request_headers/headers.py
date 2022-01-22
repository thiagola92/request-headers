import hashlib


def clean_headers(headers):
    # fields added by heroku
    headers.pop("X-Request-Id", None)
    headers.pop("X-Forwarded-For", None)
    headers.pop("X-Forwarded-Proto", None)
    headers.pop("X-Forwarded-Port", None)
    headers.pop("Via", None)
    headers.pop("Connect-Time", None)
    headers.pop("X-Request-Start", None)
    headers.pop("Total-Route-Time", None)


def get_headers_digest(headers):
    headers_bytes = bytes(str(headers), encoding="utf8")
    md5 = hashlib.md5()
    md5.update(headers_bytes)

    return md5.hexdigest()
