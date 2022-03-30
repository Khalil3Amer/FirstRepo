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
    def getName(self):
        return self.__name
    def getManger(self):
        return self.__manger
    def getDepartmentId(self):
        return self.__departmentId
    def setName(self,name):
        self.__name=name
    def setManger(self,manger):
        self.__manger=manger
    def setDepartmentId(self,id):
        self.__departmentId=id
    