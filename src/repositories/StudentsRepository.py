from entities.Student import Students
from utilities.Connection import Base, engine, session_local  

class StudentsRepository:
    def __init__(self):
        Base.metadata.create_all(engine)
        self.db = session_local()
        
    def listStudents(self):
        return self.db.query(Students).all()
        
    
    def searchStudent(self, id):
        return self.db.query(Students).filter(Students.id == id).first()
    
    def updateStudent(self, student : Students):
        self.db.commit()
        return student
    
    def deleteStudent(self, student : Students):
        self.db.delete(student)
        self.db.commit()
        
    
    def createStudent(self, student : Students):
        self.db.add(student)
        self.db.commit()
        return student
    
         