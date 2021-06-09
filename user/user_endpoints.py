from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

import datetime
from typing import List

from core.utils import get_db
from .auth import AuthHandler
from . schemas import UserCreate, UserDetail, UserLogin
from .models import User


router = APIRouter()
auth_handler = AuthHandler()


@router.get('/', status_code=200, response_model=List[UserDetail])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.post('/register', status_code=201, response_model=UserDetail)
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    hashed_password = auth_handler.get_password_hash(user_data.password)
    user_data.password = hashed_password

    user = User(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hashed_password,
    )
    try:
        db.add(user)
        db.commit()
    except IntegrityError:
        raise HTTPException(status_code=400, detail='Email is taken!')
    else:
        db.refresh(user)
        return user

    # query = User.insert().values(**user.dict)
    # return await db.execute(query)
    # return


@router.post('/login')
def login(login_data: UserLogin, db: Session = Depends(get_db)):
        user = db.query(User).filter(User.email == login_data.email).first()
        if (user is None) or (not auth_handler.verify_password(login_data.password, user.hashed_password)):
            raise HTTPException(status_code=401, detail='Invalid username and/or password')
        token = auth_handler.encode_token(user.id)

        # query = users.select().where(users.c.email==login_data.email)
        #user = await self.database.fetch_one(query)
        return { 'token': token }

@router.get('/me', response_model=UserDetail)
def get_detail_user(user_id=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == user_id).first()
