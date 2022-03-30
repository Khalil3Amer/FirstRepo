from Person import Person
class Student(Person):
    #Private
    __studentId=0
    __GPA=0.0
    __courses=[]
    #Public
    def __init__(self, id, name, bd, email, address, department, studentId,GPA,courses) -> None:
        super().__init__(id, name, bd, email, address, department)
        self.__studentId=studentId
        self.__GPA=GPA
        self.__courses= courses if courses != None else self.__courses
    def getCustomId(self):
        return self.__studentId
    
    def getStudentId(self) -> int:
        return self.__studentId
    def getGPA(self) -> float:
        return self.__GPA
    def getCourses(self) -> list:
        return self.__courses
    
    def setStudentId(self,id) -> None:
        self.__studentId=id
    def setGPA(self,GPA) -> None:
        self.__GPA=GPA
    def setCourses(self,courses) -> None:
        self.__courses=courses
    def addCourse(self,course) -> None:
        self.__courses.append(course)
    
    