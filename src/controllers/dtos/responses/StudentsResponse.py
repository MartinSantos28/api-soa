class StudentsResponse:
    def __init__(self, id , name):
        self.__id = id 
        self.__name = name  
        
    def create_Json_Data(self):
        return {'id': self.__id,'name' : self.__name}