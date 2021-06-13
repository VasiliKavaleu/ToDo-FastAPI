from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship, backref

from datetime import datetime

from sqlalchemy.sql.schema import Table

from core.db import Base


todos_tags = Table('todos_tags', Base.metadata,
    Column('todo_id', Integer, ForeignKey('todo.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
    )


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    todos = relationship("Todo",
                        secondary=todos_tags,
                        back_populates="tags")


tags = Tag.__table__
