from pydantic import BaseModel

from datetime import datetime


class TodoBase(BaseModel):
    title: str
    description: str
    important: bool
    created_at: datetime

    class Config:
      orm_mode = True


class TodoCreate(TodoBase):
  ...

  class Config:
      orm_mode = True


class TodoList(TodoBase):
    id: int


class TodoDetail(TodoList):
    ...

    # class Config:
    #   orm_mode = True


class TodoUpdate(BaseModel):
    title: str
    description: str
    important: bool

    class Config:
      orm_mode = True
