from abc import ABC, abstractmethod
from controllers.dtos.requests.TeacherRequest import CreateTeacherRequest
from controllers.dtos.requests.TeacherRequest import UpdateTeacherRequest
from entities.Teacher import Teachers

class ITeacherService(ABC):
    
    @abstractmethod
    def getAllTeachers(self):
        pass
    
    @abstractmethod
    def getTeacherById(self, id):
        pass
    
    @abstractmethod
    def createTeacher(self, teacher : Teachers):
        pass
    
    @abstractmethod 
    def updateTeacher(self, teacher : Teachers):
        pass
    
    @abstractmethod
    def deleteTeacher(self,id):
        pass