
from flask import Blueprint, request
from services.TeacherServiceImpl import TeacherServiceImpl
from controllers.StudentController import StudentService
from controllers.dtos.requests.TeacherRequest.CreateTeacherRequest import CreateTeacherRequest
from controllers.dtos.requests.TeacherRequest.UpdateTeacherRequest import UpdateTeacherRequest


TeacherService = TeacherServiceImpl()

teachers_routes = Blueprint('teachers_routes' , __name__)

@teachers_routes.route('/teachers/', methods = ['POST'])
def createTeacher():
    data = request.get_json()
    create_request = CreateTeacherRequest(data['name'], data['last_name'], data['assigment'])
    teacher = TeacherService.createTeacher(create_request)
    return {'teachers' : teacher}

@teachers_routes.route('/teachers/', methods = ['GET'])
def ListTeachers():
    list = TeacherService.getAllTeachers()
    return { 'teachers' : list}

@teachers_routes.route('/teachers/<int:id>',methods = ['GET'])
def TeacherById(id):
    teacher = TeacherService.getTeacherById(id)
    return {'teachers' : teacher}

@teachers_routes.route('/teachers/', methods=['PUT'])
def updateTeacher(id):
    data = request.get_json()
    update_request = UpdateTeacherRequest(id,data['name'], data['last_name'], data['assigment'])
    teacher = TeacherService.updateTeacher(update_request)
    return {'teacher' : teacher}

@teachers_routes.route('/teachers/<int:id>', methods = ['DELETE'])
def deleteTeacher(id):
    TeacherService.deleteTeacher(id)
    return {'message' : 'Maestro Eliminado'}