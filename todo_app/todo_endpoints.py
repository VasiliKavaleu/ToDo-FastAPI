from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

import datetime
from typing import List

from core.utils import get_db
from user.auth import AuthHandler
from . schemas import TodoCreate, TodoBase
# from .models import todo


router = APIRouter()
auth_handler = AuthHandler()


@router.post('/', response_model=TodoBase)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db), user_id=Depends(auth_handler.auth_wrapper)):
  # todo = todo.insert().values(**todo.dict(), owner_id=user_id)
  # pk = db.execute(todo)
  # return {**todo.dict(), "id": pk, "owner": {"id": user_id}}
  return {'er': 'erg'}