# coding=utf-8

from httplib import NOT_FOUND
from json import dumps


def rest(start_response, data):
    s = dumps(data)

    start_response("200 OK", [
        ("Cache-Control", "no-cache"),
        ("Content-Type", "application/json; charset=utf-8"),
        ("Content-Length", str(len(s)))
    ])

    return (s,)


def not_found(start_response):
    s = "not found!"

    start_response("{0} Not Found".format(NOT_FOUND), [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(s)))
    ])

    return s
