from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session


from typing import List

from core.utils import get_db
from user.auth import AuthHandler
from todo_app.schemas import TodoCreate, TodoList, TodoDetail, TodoUpdate
from todo_app.models import todo
from core.db import database


router = APIRouter()
auth_handler = AuthHandler()


@router.get('/todo', response_model=List[TodoList])
async def get_todo_of_user(db: Session = Depends(get_db),
                    user_id=Depends(auth_handler.auth_wrapper)):
    query = todo.select()
    resp = await database.fetch_all(query)
    print(resp)
    return resp

