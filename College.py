from Department import Department
from Student import Student
from Instructor import Instructor


def main():
    departments = []
    x = open("Data/Departments.txt")
    for line in x:
        line = line.split(" ")
        departments.append(Department(line[0], None, line[1].rstrip()))
    x.close()

    students = []
    x = open("Data/Students.txt")
    for line in x:
        line = line.split(" ")
        students.append(
            Student(
                line[0],
                line[1],
                line[2],
                line[3],
                line[4],
                None,
                line[5],
                float(line[6]),
                line[7].strip().split(","),
            )
        )
    students[0].setDepartment(departments[0])
    students[1].setDepartment(departments[1])
    x.close()

    instructors = []
    x = open("Data/Instructors.txt")
    for line in x:
        line = line.split(" ")
        instructors.append(
            Instructor(
                line[0],
                line[1],
                line[2],
                line[3],
                line[4],
                None,
                line[5],
                float(line[6]),
                line[7],
                None,
                line[8],
                line[9],
            )
        )
    x.close()

    print("*********** instructors ***************")
    for i in instructors:
        print(i)

    print("*********** departments ***************")
    for i in departments:
        print(i)

    print("*********** students ***************")
    for i in students:
        print(i)


if __name__ == "__main__":
    main()
