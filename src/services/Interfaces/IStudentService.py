from abc import ABC, abstractmethod
from controllers.dtos.requests.StudentRequest.CreateStudentRequest import CreateStudentRequest
from controllers.dtos.requests.StudentRequest.UpdateStudentRequest import UpdateStudentRequest
from entities.Student import Students

class IStudentService(ABC):
    @abstractmethod
    def getAllStudents(self):
        pass 
        
    @abstractmethod
    def getStudentById(self, id ):
        pass
    
    @abstractmethod
    def createStudent(self, student:Students):
        pass
    
    @abstractmethod
    def updateStudent(self, student : Students):
        pass 
    
    @abstractmethod
    def deleteStudent(self, id): 
        pass 