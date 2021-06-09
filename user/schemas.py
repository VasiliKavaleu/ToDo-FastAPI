from pydantic import BaseModel,  EmailStr, validator, constr


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class UserDetail(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=5)
    password2: str

    @validator("password2")
    def password_match(cls, password2, values, **kwargs):
        if 'password' in values and password2 != values["password"]:
            raise ValueError("Passwords don't match")
        return password2

