from pydantic import BaseModel

from datetime import datetime
from typing import List

from tags.schemas import TagId, TagList


class TodoBase(BaseModel):
    title: str
    description: str
    important: bool
    created_at: datetime

    class Config:
        orm_mode = True


class TodoCreate(TodoBase):
    ...
    tags: List[TagId]

    class Config:
        orm_mode = True


class TodoList(TodoBase):
    id: int
    tags: List[TagList]


class TodoDetail(TodoList):
    ...
    tags: List[TagList]


class TodoUpdate(BaseModel):
    title: str
    description: str
    important: bool
    tags: List[TagId]

    class Config:
        orm_mode = True
