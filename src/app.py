from flask import Flask
from controllers.StudentController import students_routes 
from flask_cors import CORS   # type: ignore
from controllers.TeacherController import teachers_routes
app = Flask(__name__)
app.register_blueprint(students_routes) 
app.register_blueprint(teachers_routes)


CORS(app)

if __name__ == '__main__' : 
    app.run(debug=True, port=8080)
