from fastapi import HTTPException

from user.models import User
from .models import Todo


def get_users_todo(db, user_id):
  user = db.query(User).filter_by(id=user_id).one()
  return user.todo


def create_users_todo(db, user_id, payload):
  new_todo = Todo(**payload.dict(), owner_id=user_id)
  db.add(new_todo)
  db.commit()
  db.refresh(new_todo)
  return new_todo


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
  return {'id': todo_id, **payload.dict()}
