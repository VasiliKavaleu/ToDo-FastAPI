from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session

from typing import List

from core.utils import get_db
from user.auth import AuthHandler
from .schemas import BookList, ReaderCreate, BookCreate, CoverCreate, ReadersBook, ReviewCreate, ReaderBookResponse, Readers
from .models import Book, Cover, Reader, Review, ReaderBook

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


@router.get('/readers', response_model=List[Readers])
def get_all_reader(db: Session = Depends(get_db)):
    return db.query(Reader).all()


@router.get('/cover')
def get_all_covers(db: Session = Depends(get_db)):
    return db.query(Cover).all()


@router.post('/book/{pk}/cover')
def create_cover(pk: int, payload: CoverCreate, db: Session = Depends(get_db)):
    """ Creating a cover for book """
    book = db.query(Book).get(pk)
    if not book:
        raise HTTPException(status_code=400, detail='Books not found!')
    cover = Cover(
                image=payload.image,
                artist=payload.artist
                )

    if book.cover:
        raise HTTPException(status_code=400, detail='Books already have a cover!')

    db.add(cover)
    book.cover = cover
    db.commit()
    db.refresh(cover)
    return cover


@router.post('/book/{book_id}/reviews/{user_id}')
def create_review_for_book(book_id: int, user_id: int, payload: ReviewCreate, db: Session = Depends(get_db)):
    review = Review(
        text=payload.text,
        book_id=book_id,
        user_id=user_id
    )
    db.add(review)
    db.commit()
    db.refresh(review)
    return review


@router.post('/user/{user_id}/book/{book_id}')
def adding_book_to_user(book_id: int, user_id: int, db: Session = Depends(get_db)):
    user = db.query(Reader).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found!')
    book = db.query(Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail='Book not found!')
    user.books.append(book)
    db.commit()
    return {"Result": f"Books with id:{book_id} successfull added to user id:{user_id}"}
