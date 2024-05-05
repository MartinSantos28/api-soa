from controllers.dtos.requests.TeacherRequest.CreateTeacherRequest import CreateTeacherRequest
from controllers.dtos.requests.TeacherRequest.UpdateTeacherRequest import UpdateTeacherRequest
from services.Interfaces.ITeacherService import ITeacherService
from controllers.dtos.responses.TeacherResponse import TeacherResponse
from entities.Teacher import Teachers 
from repositories.TeacherRepository import TeachersRepository

class TeacherServiceImpl(ITeacherService):
    
    def __init__(self):
        self.repository = TeachersRepository()
        
    def getAllTeachers(self):
        return [self.generated_response(t) for t in self.repository.listTeachers()]
    
    def getTeacherById(self, id):
        return self.generated_response(self.repository.searchTeacher(id))

    def createTeacher(self, request : CreateTeacherRequest): 
        teacher = Teachers(name = request.getName(), last_name = request.getLast_Name(), assigment = request.getAssigment())
        return self.generated_response(self.repository.createTeacher(teacher))
    
    def updateTeacher(self, request : UpdateTeacherRequest):
        teacher = self.find_and_ensure_if_exist(request.getId())
        teacher.name = request.getName()
        teacher.last_name = request.getLast_Name()
        teacher.assigment = request.getAssigment()
        return self.generated_response(self.repository.updateTeacher(teacher))
    
    def deleteTeacher(self, id):
        teacher = self.find_and_ensure_if_exist(id)
        self.repository.deleteTeacher(teacher)

    def generated_response(self, t):
        response = TeacherResponse(t.id, t.name, t.last_name, t.assigment)
        return response.create_Json_Data()
    
    def find_and_ensure_if_exist(self, id) -> Teachers:
        return self.repository.searchTeacher(id)