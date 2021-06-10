from fastapi import FastAPI, Depends, HTTPException, APIRouter, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

import datetime
from typing import List

from core.utils import get_db
from user.auth import AuthHandler
from . schemas import TodoCreate, TodoBase, TodoList, TodoDetail, TodoUpdate
from .models import todo, Todo
from user.models import User

router = APIRouter()
auth_handler = AuthHandler()


@router.post('/', response_model=TodoDetail)
def create_todo(todo_data: TodoCreate, db: Session = Depends(get_db), user_id=Depends(auth_handler.auth_wrapper)):
  # todo_query = todo.insert().values(**todo_data.dict(), owner_id=user_id)
  # pk = db.execute(todo_query)
  # return {**todo_data.dict(), "id": pk, "owner": {"id": user_id}}
  new_todo = Todo(**todo_data.dict(), owner_id=user_id)
  db.add(new_todo)
  db.commit()
  db.refresh(new_todo)
  return new_todo


@router.get('/', response_model=List[TodoList])
def get_todo_of_user(db: Session = Depends(get_db), user_id=Depends(auth_handler.auth_wrapper)):
  user = db.query(User).filter_by(id=user_id).one()
  return user.todo


@router.delete('/{pk}', status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(pk: int, db: Session = Depends(get_db), user_id=Depends(auth_handler.auth_wrapper)):
  user_todo = db.query(Todo).filter_by(owner_id=user_id, id=pk).first()
  if not user_todo:
    raise HTTPException(status_code=404, detail='ToDo not found')
  db.delete(user_todo)
  db.commit()
  return


@router.put('/{pk}', status_code=status.HTTP_200_OK)
def todo_update(pk: int, payload: TodoUpdate, db: Session = Depends(get_db), user_id=Depends(auth_handler.auth_wrapper)):
  user_todo = db.query(Todo).filter_by(owner_id=user_id, id=pk).update(payload.dict())
  if not user_todo:
    raise HTTPException(status_code=404, detail='ToDo not found')
  db.commit()
  return {'id': pk, **payload.dict()}




