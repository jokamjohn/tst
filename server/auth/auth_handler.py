import time
from typing import Dict

import jwt
from decouple import config

from server.models.user import UserSchema

users = []

JWT_SECRET = config("JWT_SECRET")
JWT_ALGORITHM = config("JWT_ALGORITHM")


def token_response(token: str):
    return {
        "token": token
    }


def sign_jwt(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return token_response(token)


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}


def verify_jwt(token: str) -> bool:
    try:
        payload = decode_jwt(token)
        if payload:
            return True
    except:
        return False


def verify_user(data: UserSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False
