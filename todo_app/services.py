from fastapi import HTTPException

from sqlalchemy import and_

from user.models import User
from tags.services import get_tags_by_id
from tags.models import Tag, tags, todos_tags
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
      todo.tags.append(get_tags_by_id(db, tag['id']))
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
  data = payload.dict()
  tags = data.pop('tags')
  user_todo = db.query(Todo).filter_by(owner_id=user_id, id=todo_id).update(data)
  if not user_todo:
    raise HTTPException(status_code=404, detail='ToDo not found')

  todo = get_todo_by_id(db, todo_id)
  if tags:
    tags_id = []
    for tag in tags:
      todo.tags.append(get_tags_by_id(db, tag['id']))
      tags_id.append(tag['id'])
      db.add(todo)
  
  tags_obj = db.query(Tag).filter(Tag.id.notin_(tags_id)).all()
  for tag_obj in tags_obj:
    try:
      todo.tags.remove(tag_obj)
    except ValueError:
      pass

  q = db.query(Todo, Tag).filter(and_(
    todos_tags.c.todo_id == Todo.id,
    todos_tags.c.tag_id == Tag.id,
  ))

  db.commit()
  return todo


def get_tags_todo(db, tag_id):
  return get_tags_by_id(db, tag_id).todos
