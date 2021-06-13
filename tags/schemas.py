from pydantic import BaseModel
from pydantic.errors import cls_kwargs


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    ...


class TagList(TagBase):
    id: int

    class Config:
        orm_mode = True

class TagId(BaseModel):
    id: int
