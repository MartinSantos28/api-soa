from sqlalchemy import Column, Integer, String
from utilities.Connection import Base 

class Teachers(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    assigment = Column(String(50),nullable=False)