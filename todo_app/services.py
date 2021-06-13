from fastapi import HTTPException

from user.models import User
from tags.services import get_tags_by_id
from .models import Todo


def get_users_todo(db, user_id):
  user = db.query(User).filter_by(id=user_id).one()
  return user.todo


def get_todo_by_id(db, todo_id):
  return db.query(Todo).get(todo_id)


def create_users_todo(db, user_id, payload):
  data = payload.dict()
  tags = data.pop('tags')
  todo = Todo(**data, owner_id=user_id)
  db.add(todo)
  if tags:
    for tag in tags:
      todo.tags.append(get_tags_by_id(db, tag))
      db.add(todo)
  db.commit()
  db.refresh(todo)
  return todo


def delete_users_todo(db, user_id, todo_id):
  user_todo = db.query(Todo).filter_by(owner_id=user_id, id=todo_id).first()
  if not user_todo:
    raise HTTPException(status_code=404, detail='ToDo not found')
  db.delete(user_todo)
  db.commit()


def update_users_todo(db, user_id, todo_id, payload):
  user_todo = db.query(Todo).filter_by(owner_id=user_id, id=todo_id).update(payload.dict())
  if not user_todo:
    raise HTTPException(status_code=404, detail='ToDo not found')
  db.commit()
  return get_todo_by_id(db, todo_id)
