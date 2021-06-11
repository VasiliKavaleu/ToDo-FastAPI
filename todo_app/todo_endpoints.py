from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session

from typing import List

from core.utils import get_db
from user.auth import AuthHandler
from . schemas import TodoCreate, TodoList, TodoDetail, TodoUpdate
from . import services


router = APIRouter()
auth_handler = AuthHandler()


@router.post('/', response_model=TodoDetail)
def create_todo(payload: TodoCreate, 
                db: Session = Depends(get_db), 
                user_id=Depends(auth_handler.auth_wrapper)):
  return services.create_users_todo(db, user_id, payload)


@router.get('/', response_model=List[TodoList])
def get_todo_of_user(db: Session = Depends(get_db), 
                    user_id=Depends(auth_handler.auth_wrapper)):
  return services.get_users_todo(db, user_id)


@router.delete('/{pk}', status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(pk: int, 
                db: Session = Depends(get_db), 
                user_id=Depends(auth_handler.auth_wrapper)):
  return services.delete_users_todo(db, user_id, pk)


@router.put('/{pk}', status_code=status.HTTP_200_OK)
def todo_update(pk: int, 
                payload: TodoUpdate, 
                db: Session = Depends(get_db), 
                user_id=Depends(auth_handler.auth_wrapper)):
  return services.update_users_todo(db, user_id, pk, payload)
