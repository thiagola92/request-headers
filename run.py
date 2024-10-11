import json
import logging

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.routing import Route
from starlette.responses import FileResponse, PlainTextResponse

from request_headers.headers import save_headers
from request_headers.website import website

logging.basicConfig(
    filename=None, level=logging.INFO, format="%(levelname)s:     %(message)s"
)


async def homepage(request: Request):
    headers = save_headers(request)
    return PlainTextResponse(json.dumps(headers, indent=2))


async def image_png(request: Request):
    save_headers(request)
    return FileResponse("contents/image.png")


async def image_jpg(request: Request):
    save_headers(request)
    return FileResponse("contents/image.jpg")


async def favicon(request: Request):
    save_headers(request)
    return FileResponse("contents/favicon.png")


async def image_link(request: Request):
    save_headers(request)
    return FileResponse("contents/image_link.png")


async def code_js(request: Request):
    save_headers(request)
    return FileResponse("contents/code.js")


async def style_css(request: Request):
    save_headers(request)
    return FileResponse("contents/style.css")


routes = [
    Route("/", endpoint=homepage),
    Route("/website", endpoint=website),
    Route("/image.png", endpoint=image_png),
    Route("/image.jpg", endpoint=image_jpg),
    Route("/favicon.png", endpoint=favicon),
    Route("/image_link.png", endpoint=image_link),
    Route("/code.js", endpoint=code_js),
    Route("/style.css", endpoint=style_css),
]

app = Starlette(debug=True, routes=routes)
