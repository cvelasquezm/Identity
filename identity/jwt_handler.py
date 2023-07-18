import time
import jwt
from decouple import config
from jwt import ExpiredSignatureError

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def token_response(token: str):
    return {
        "access token": token
    }


def sign_jwt(username: str):
    payload = {
        "username": username,
        "exp": time.time() + 60
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decode_jwt(token: str):
    try:
        body = jwt.decode(token, JWT_SECRET, options={"verify_signature": True}, algorithms=[JWT_ALGORITHM])
        username = body["username"]

    except ExpiredSignatureError as e:
        raise Exception("The signature has expired")
