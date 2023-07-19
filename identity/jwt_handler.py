import time
from os import environ

import jwt
from jwt import ExpiredSignatureError
from pydantic import constr, conint

JWT_SECRET: constr(min_length=1) = environ["JWT_SECRET"]
JWT_ALGORITHM: constr(min_length=1) = environ["JWT_ALGORITHM"]
JWT_EXP_TIME: conint(gt=0) = int(environ["JWT_EXP_TIME"])


def token_response(token: str):
    return {
        "access token": token
    }


def sign_jwt(username: str):
    payload = {
        "username": username,
        "exp": time.time() + JWT_EXP_TIME
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decode_jwt(token: str):
    try:
        body = jwt.decode(token, JWT_SECRET, options={"verify_signature": True}, algorithms=[JWT_ALGORITHM])
        username = body["username"]

    except ExpiredSignatureError as e:
        raise Exception("The signature has expired")
