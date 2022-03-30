from abc import ABC,abstractmethod
from Department import Department
class Person(ABC):
    #Private
    __id=0
    __name=""
    __bd=""
    __email=""
    __address=""
    __department=None
    #Public
    def __init__(self,id,name,bd,email,address,department) -> None:
        self.__id=id
        self.__name=name
        self.__bd=bd
        self.__email=email
        self.__address=address
        self.__department=department
    @abstractmethod
    def getCustomId(self):
        pass
    def setId(self,id) -> None:
        self.__id=id
    def setName(self,name) -> None:
        self.__name=name
    def setBD(self,bd) -> None:
        self.__bd=bd
    def setEmail(self,email) -> None:
        self.__email=email
    def setAddress(self,address) -> None:
        self.__address=address
    def setDepartment(self,department) -> None:
        self.__department=department


    def getId(self) -> int:
        return self.__id
    def getName(self) -> str:
        return self.__name
    def getBD(self) -> str:
        return self.__bd
    def getEmail(self) -> str:
        return self.__email
    def getAddress(self) -> str:
        return self.__address
    def getDepartment(self) -> Department:
        return self.__department
    
    def __str__(self) -> str:
        return f'Id = {self.__id}, Name = {self.__name}, BirthDate = {self.__bd}, Email = {self.__email}, Address = {self.__address}, Department = {self.__department}'