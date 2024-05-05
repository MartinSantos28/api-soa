
from entities.Teacher import Teachers
from utilities.Connection import Base, engine, session_local

class TeachersRepository:
    def __init__(self):
        Base.metadata.create_all(engine)
        self.db = session_local()
        
    def listTeachers(self):
        return self.db.query(Teachers).all()
    
    def searchTeacher(self, id ): 
        return self.db.query(Teachers).filter(Teachers).first()
    
    def updateTeacher(self , teacher : Teachers):
        self.db.commit()
        return teacher
    
    def deleteTeacher(self, teacher : Teachers ):
        self.db.delete(teacher)
        self.db.commit()
        
    def createTeacher(self, teacher : Teachers):
        self.db.add(teacher)
        self.db.commit
        return teacher