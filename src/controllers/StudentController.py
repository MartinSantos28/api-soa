from flask import Blueprint, request
from services.StudentServiceImpl import StudentServiceImpl
from controllers.dtos.requests.StudentRequest.CreateStudentRequest import CreateStudentRequest
from controllers.dtos.requests.StudentRequest.UpdateStudentRequest import UpdateStudentRequest


StudentService = StudentServiceImpl()

students_routes = Blueprint('students_routes',__name__) 

@students_routes.route('/students/', methods = ['GET'])
def ListStudent():
    list = StudentService.getAllStudents()
    return {'students' : list}
    
@students_routes.route('/students/<int:id>', methods=['GET'])
def StudentById(id):
    student =  StudentService.getStudentById(id)
    return {'students' : student}

@students_routes.route('/students/', methods=['POST'])
def createStudent():
    data = request.get_json()
    create_request = CreateStudentRequest(data['name'])
    student = StudentService.createStudent(create_request)
    return {'students' : student}


@students_routes.route('/students/<int:id>', methods=['PUT'])
def updateStudent(id):
    data = request.get_json()
    update_request = UpdateStudentRequest(id, data['name'])
    student = StudentService.updateStudent(update_request)
    return {'student' : student}

@students_routes.route('/students/<int:id>', methods = ['DELETE'])
def deleteStudent(id):
    StudentService.deleteStudent(id)
    return {'message': 'Estudiante Eliminado'}