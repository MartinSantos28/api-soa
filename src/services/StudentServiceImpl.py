from repositories.StudentsRepository import StudentsRepository
from controllers.dtos.requests.StudentRequest.CreateStudentRequest import CreateStudentRequest
from controllers.dtos.requests.StudentRequest.UpdateStudentRequest import UpdateStudentRequest
from services.Interfaces.IStudentService import IStudentService
from controllers.dtos.responses.StudentsResponse import StudentsResponse
from entities.Student import Students
class StudentServiceImpl(IStudentService):
    
    def __init__(self):
        self.repository = StudentsRepository()
        
    
    def getAllStudents(self):
        return [self.generated_response(s) for s in self.repository.listStudents()]
    
    
    def getStudentById(self, id ):
        return self.generated_response(self.repository.searchStudent(id))
    
    
    def createStudent(self, request : CreateStudentRequest):
        student = Students(name=request.getName())
        return self.generated_response(self.repository.createStudent(student))
    
    
    def updateStudent(self, request : UpdateStudentRequest):
        student = self.find_and_ensure_if_exist(request.getId())
        student.name = request.getName()
        return self.generated_response(self.repository.updateStudent(student))
    
    
    def deleteStudent(self, id): 
        student = self.find_and_ensure_if_exist(id)
        self.repository.deleteStudent(student)
        
    def generated_response(self,s):
        response = StudentsResponse(s.id,s.name)
        return response.create_Json_Data()
    
    def find_and_ensure_if_exist(self,id) -> Students:
        return self.repository.searchStudent(id)
        
        
        