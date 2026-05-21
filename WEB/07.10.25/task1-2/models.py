from sqlalchemy import Column, Integer, String, Boolean
from db import Base


class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    adopted = Column(Boolean, default=False)

    # #task2
    # health_status = Column(String, default="healthy")