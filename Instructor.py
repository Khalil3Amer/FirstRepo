from Staff import Staff


class Instructor(Staff):
    # Private
    __major = ""
    __degree = ""
    # Public

    def __init__(
        self,
        id,
        name,
        bd,
        email,
        address,
        department,
        empId,
        salary,
        postion,
        superVisor,
        major,
        degree,
    ) -> None:
        super().__init__(
            id,
            name,
            bd,
            email,
            address,
            department,
            empId,
            salary,
            postion,
            superVisor,
        )
        self.__major = major
        self.__degree = degree

    def getCustomId(self) -> int:
        return self.__empId

    def getMajor(self) -> str:
        return self.__major

    def getDegree(self) -> str:
        return self.__degree

    def setMajor(self, major) -> None:
        self.__major = major

    def setDegree(self, degree) -> None:
        self.__degree = degree

    def __str__(self) -> str:
        return (
            super().__str__()
            + f", Major = {self.__major}, Degree = {self.__degree}"
        )
