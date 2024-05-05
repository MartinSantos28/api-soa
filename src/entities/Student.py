from sqlalchemy import Column, Integer, String
from utilities.Connection import Base 
from sqlalchemy.sql import func

class Students(Base): # type: ignore
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50),nullable=False)