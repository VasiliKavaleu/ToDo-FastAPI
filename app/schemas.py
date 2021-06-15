from pydantic import BaseModel

from datetime import datetime
from typing import List


class Cover(BaseModel):
    id: int
    image: str
    artist: str


class CoverCreate(BaseModel):
    image: str
    artist: str


class ReviewList(BaseModel):
    title: str


class ReaderCreate(BaseModel):
    name: str


class ReaderBook(BaseModel):
    id: int
    name: str


class BookList(BaseModel):
    id: str
    title: str
    author: str
    want_to_read: bool

    reviews: List[ReviewList]
    readers: List[ReaderBook]
    cover: Cover = None


    class Config:
        orm_mode = True


class BookCreate(BaseModel):
    title: str
    author: str


