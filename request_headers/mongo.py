import os
from pymongo import MongoClient
from request_headers.headers import get_headers_digest

uri = os.environ["MONGO_URI"]


def find_headers_digest(headers_digest):
    client = MongoClient(uri)
    collection = client["headers"]["headers"]

    return collection.find_one({"digest": headers_digest})


def insert_headers(headers):
    client = MongoClient(uri)
    collection = client["headers"]["headers"]
    headers_digest = get_headers_digest(headers)

    if find_headers_digest(headers_digest):
        return

    collection.insert_one({"digest": headers_digest, "headers": headers})
