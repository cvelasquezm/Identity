from fastapi import FastAPI, Body, HTTPException, status
from identity.jwt_handler import sign_jwt, decode_jwt
from identity.schemas import UserLoginSchema, UserSchema

api = FastAPI()

users: list[UserSchema] = [
    UserSchema(fullname="Cesar Andres Velasquez Martinez", email="cesarandresvelasquez@gmail.com", password="123"),
    UserSchema(fullname="Leaniceth Quintana Guerrero", email="leaniceth.quintana@gmail.com", password="123"),
]


def check_user(data: UserLoginSchema):
    for user in users:
        return user.email == data.email and user.password == data.password


@api.post("/login")
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return sign_jwt(user.email)
    else:
        return {
            "error": "wrong login details!!!"
        }


@api.get("/decode")
def decode(token: str):
    try:
        decode_jwt(token)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE) from e
