from pydantic import BaseModel

from datetime import datetime
from typing import List


class BookForReaders(BaseModel):
    id: int
    title: str
    author: str

    class Config:
        orm_mode = True

class Cover(BaseModel):
    id: int
    image: str
    artist: str

    class Config:
        orm_mode = True


class CoverCreate(BaseModel):
    image: str
    artist: str


class ReviewList(BaseModel):
    id: int
    text: str

    class Config:
        orm_mode = True


class ReaderCreate(BaseModel):
    name: str


class Readers(BaseModel):
    id: int
    name: str
    books: List[BookForReaders] = None

    class Config:
        orm_mode = True


class ReadersBook(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class BookList(BaseModel):
    id: str
    title: str
    author: str
    want_to_read: bool

    reviews: List[ReviewList]
    readers: List[ReadersBook]
    cover: Cover = None

    class Config:
        orm_mode = True


class BookCreate(BaseModel):
    title: str
    author: str


class ReviewCreate(BaseModel):
    text: str


class ReaderBookResponse(BaseModel):
    user_id: int
    book_id: int
