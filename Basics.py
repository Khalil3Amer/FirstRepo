from abc import ABC
from abc import abstractmethod
import re


class Empolyee(ABC):
    # Protected
    _empId = 0
    # Private
    __name = ""
    __id = 0
    __phones = []
    __salary = 0.0
    # Public
    def __init__(self, empId, name, id, *phones) -> None:
        self._empId = empId
        self.__name = name
        self.__id = id
        for phone in phones:
            self.addPhone(phone)

    @abstractmethod
    def getSalary(self):
        pass

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getId(self):
        return self.__id

    def getPhones(self):
        return self.__phones

    def addPhone(self, phone):
        if phone not in self.__phones:
            self.__phones.append(phone)

    def removePhone(self, phone):
        if phone in self.__phones:
            self.__phones.remove(phone)


class SalariedEmployee(Empolyee):
    # Private
    __monthlySalary = 0.0
    # Public
    def __init__(self, monthlySalay, empId, name, id, *phones) -> None:
        super().__init__(empId, name, id, *phones)
        self.__monthlySalary = monthlySalay

    def getSalary(self):
        return self.__monthlySalary


class HourlyEmployee(Empolyee):
    # Private
    __hours = {}  # to keep track of the hours the employee worked each day
    __perHour = 0.0
    # Public
    def __init__(self, perHour, empId, name, id, *phones) -> None:
        super().__init__(empId, name, id, *phones)
        self.__perHour = perHour

    def getSalary(self):
        sum = 0.0
        for i in self.__hours.values():
            sum += i * self.__perHour
        return sum

    def addHours(self, date, hours):  # date in format dd-mm-yyyy
        if (
            re.search(
                "^(0?[1-9]||3[01]||[12][0-9])-(0?[1-9]||1[0-2])-[0-9][0-9][0-9][0-9]$",
                date,
            )
            == None
        ):
            return False
        self.__hours[date] = hours
        return True

    def setPerHour(self, perHour):
        self.__perHour = perHour

    def getPerHour(self):
        return self.__perHour

    def clearHours(self):  # when the employee gets paid the work history gets cleard
        self.__hours.clear()


def main():
    pass


if __name__ == "__main__":
    main()
