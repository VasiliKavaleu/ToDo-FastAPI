from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session


from typing import List

from core.utils import get_db
from user.auth import AuthHandler
from todo_app.schemas import TodoCreate, TodoList, TodoDetail, TodoUpdate, TodoListAsyncDB
from todo_app.models import Todo, todo
from core.db import database
from tags.models import todos_tags, tags


router = APIRouter()
auth_handler = AuthHandler()


@router.get('/todo', response_model=List[TodoListAsyncDB])
async def get_todo_of_user(db: Session = Depends(get_db),
                    user_id=Depends(auth_handler.auth_wrapper)):
    query = todo.select().where(todo.c.owner_id == user_id)
    return await database.fetch_all(query)


    # query = tag.select().where(tag.c.id == )
    # query = todo.select().where(todo.c.owner_id == user_id)
    # query = query.select_from.join(todos_tags, todo.c.id == todos_tags.c.todo_id)


@router.post('/todo', response_model=TodoDetail)
async def create_todo(payload: TodoCreate,
                db: Session = Depends(get_db),
                user_id=Depends(auth_handler.auth_wrapper)):
    data = payload.dict()
    tags = data.pop('tags')
    query = todo.insert().values(**data, owner_id=user_id)
    return await database.execute(query)

