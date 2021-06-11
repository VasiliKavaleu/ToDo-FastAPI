from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session

from typing import List

from core.utils import get_db
from user.auth import AuthHandler
from . schemas import TagCreate, TagList
from . import services


router = APIRouter()
auth_handler = AuthHandler()


@router.get('/', response_model=List[TagList])
def get_tags(db: Session = Depends(get_db)):
    return services.get_tags(db)


@router.post('/', response_model=TagList)
def create_tag(payload: TagCreate, db: Session = Depends(get_db)):
    return services.create_tag(db, payload)


@router.delete('/{pk}', status_code=status.HTTP_204_NO_CONTENT)
def delete_tag(pk, db: Session = Depends(get_db)):
    return services.create_tag(db, pk)

