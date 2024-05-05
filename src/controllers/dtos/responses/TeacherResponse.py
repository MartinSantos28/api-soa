class TeacherResponse:
    def __init__(self, id , name , last_name, assigment):
        self.__id = id 
        self.__name = name 
        self.__last_name = last_name
        self.__assigment = assigment
        
    def create_Json_Data(self):
        return {'id': self.__id,'name' : self.__name, 
                'last_name' : self.__last_name, 'assigment' : self.__assigment}