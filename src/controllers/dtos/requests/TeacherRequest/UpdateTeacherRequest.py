class UpdateTeacherRequest:
    def __init__(self, id , name , last_name, assigment):
        self.__id = id 
        self.__name = name 
        self.__last_name = last_name
        self.__assigment = assigment
        
    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getLast_Name(self):
        return self.__last_name
    
    def getAssigment(self):
        return self.__assigment