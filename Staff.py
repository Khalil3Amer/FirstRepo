from Person import Person
class Staff(Person):
    #Private
    __empId=0
    __salary=0.0
    __postion=""
    __superVisor=None
    #Public
    def __init__(self, id, name, bd, email, address, department,empId,salary,postion,superVisor) -> None:
        super().__init__(id, name, bd, email, address, department)
        self.__empId=empId
        self.__salary=salary
        self.__postion=postion
        self.__superVisor=superVisor
    def getEmpId(self) -> int:
        return self.__empId
    def getSalary(self) -> float:
        return self.__salary
    def getPosition(self) -> str:
        return self.__postion
    def getSuperVisor(self) -> Person:
        return self.__superVisor

    def setEmpId(self,id) -> None:
        self.__empId=id
    def setSalary(self,salary) -> None:
        self.__salary=salary
    def setPosition(self,positon) -> None:
        self.__postion=positon
    def setSuperVisor(self,superVisor) -> None:
        self.__superVisor=superVisor
    