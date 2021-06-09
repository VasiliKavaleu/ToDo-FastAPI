from pydantic import BaseModel

from datetime import datetime


class TodoBase(BaseModel):
    title: str
    description: str
    important: bool
    created_at: datetime


class TodoCreate(TodoBase):
  ...

  class Config:
      orm_mode = True


