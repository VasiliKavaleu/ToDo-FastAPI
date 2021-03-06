from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship, backref

from datetime import datetime

from core.db import Base
from tags.models import todos_tags


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    important = Column(Boolean)
    created_at = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", backref="todo")
    tags = relationship("Tag",
                    secondary=todos_tags,
                    back_populates="todos")


todo = Todo.__table__
