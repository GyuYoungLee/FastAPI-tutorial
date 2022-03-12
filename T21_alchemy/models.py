from sqlalchemy import Column, String, Integer

from T21_alchemy.databases import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), index=True)
    age = Column(Integer)
