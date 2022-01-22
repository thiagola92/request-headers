import hashlib


def clean_headers(headers):
    """
    I just want the basic fields that change from browser to browser.
    Anything related to what you were doing or where you came from, 
    doesn't matter to me.
    """

    # No use to know
    headers.pop("Host", None)

    # Intention context fields
    headers.pop("Cache-Control", None)
    headers.pop("Referer", None)
    headers.pop("Sec-Fetch-Site", None)
    headers.pop("Sec-Fetch-Mode", None)
    headers.pop("Sec-Fetch-User", None)
    headers.pop("Sec-Fetch-Dest", None)

    # Heroku/proxy fields
    headers.pop("Remote-Addr", None)
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
