__author__ = 'yu'
from flask import session, request


def get_remote_ip():
    x_real_ip = request.headers.get("X-Real-IP")
    if x_real_ip :
        return x_real_ip
    else:
        return request.remote_addr
