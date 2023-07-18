from pydantic import BaseModel


class UserSchema(BaseModel):
    fullname: str = None
    email: str = None
    password: str = None

    class Config:
        the_schema = {
            "user_demo": {
                "name": "Bek",
                "email": "cesar@mail.com",
                "password": "123"
            }
        }


class UserLoginSchema(BaseModel):
    email: str = None
    password: str = None

    class Config:
        the_schema = {
            "user_demo": {
                "email": "cesar@mail.com",
                "password": "123"
            }
        }
