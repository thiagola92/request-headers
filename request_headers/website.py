from pathlib import Path

from starlette.requests import Request
from starlette.responses import HTMLResponse

from request_headers.headers import save_headers


async def website(request: Request):
    save_headers(request)
    content = Path("contents/website.html").read_text()
    return HTMLResponse(content)
