from sqlalchemy import Column, String, Integer

from .databases import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)
