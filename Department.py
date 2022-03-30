class Department:
    #Private
    __departmentId=0
    __manger=None
    __name=""
    #Public
    def __init__(self,depId,manger,name) -> None:
        self.__departmentId=depId
        self.__manger=manger
        self.__name=name
    def getName(self) -> str:
        return self.__name
    def getManger(self):
        return self.__manger
    def getDepartmentId(self) -> int:
        return self.__departmentId
    def setName(self,name):
        self.__name=name
    def setManger(self,manger):
        self.__manger=manger
    def setDepartmentId(self,id):
        self.__departmentId=id
    def __str__(self) -> str:
        return f', DepartmentID = {self.__departmentId}, Name = {self.__name} , Manger = {self.__manger}'