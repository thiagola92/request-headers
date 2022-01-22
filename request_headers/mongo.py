import os
import hashlib
from pymongo import MongoClient

uri = os.environ["MONGO_URI"]


def get_headers_digest(headers):
    headers_bytes = bytes(str(headers), encoding="utf8")
    md5 = hashlib.md5()
    md5.update(headers_bytes)

    return md5.hexdigest()


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
