from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session

from typing import List

from core.utils import get_db
from user.auth import AuthHandler
from .schemas import BookList, ReaderCreate, BookCreate, CoverCreate
from .models import Book, Cover, Reader

router = APIRouter()
auth_handler = AuthHandler()


@router.get('/books', response_model=List[BookList])
def get_all_books(db: Session = Depends(get_db)):
    return db.query(Book).all()


@router.post('/books')
def create_book(payload: BookCreate, db: Session = Depends(get_db)):
    book = Book(
        title=payload.title,
        author=payload.author
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


@router.post('/readers')
def create_reader(payload: ReaderCreate, db: Session = Depends(get_db)):
    reader = Reader(
        name=payload.name
    )
    db.add(reader)
    db.commit()
    db.refresh(reader)
    return reader


@router.get('/readers')
def get_all_reader(db: Session = Depends(get_db)):
    return db.query(Reader).all()


@router.post('/book/{pk}/cover')
def create_cover(pk: int, payload: CoverCreate, db: Session = Depends(get_db)):
    book = db.query(Book).get(pk)
    if not book:
        raise HTTPException(status_code=400, detail='Books not found!')
    cover = Cover(
            image=payload.image,
            artist=payload.artist
    )

    db.add(cover)
    book.cover = cover
    db.commit()
    db.refresh(cover)
    print(book)
    return cover




