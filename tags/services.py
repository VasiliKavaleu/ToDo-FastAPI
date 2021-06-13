from tags.models import Tag
from fastapi import HTTPException


def get_tags(db):
    return db.query(Tag).all()


def create_tag(db, payload):
    new_tag = Tag(**payload.dict())
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    print(new_tag)
    return new_tag


def delete_tag(db, tag_id):
    tag = db.query(Tag).filter_by(id=tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail='Tag not found')
    db.delete(tag)
    db.commit()
