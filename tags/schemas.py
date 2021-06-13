from pydantic import BaseModel


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    ...


class TagList(TagBase):
    id: int

    class Config:
        orm_mode = True
