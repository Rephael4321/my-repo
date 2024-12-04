from utils import getNumberFromUser, getSpacer
from Person import Person


class Employee(Person):
    def __init__(
        self,
        id: int,
        name: str,
        age: int,
        field_of_work: str = None,
        salary: int = None,
    ) -> None:
        super().__init__(id, name, age)
        if field_of_work is None:
            field_of_work = input("Filed of work: ")
        if salary is None:
            salary = getNumberFromUser("Salary")
        self._field_of_work = field_of_work
        self._salary = salary

    def getFieldOfWork(self) -> str:
        return self._field_of_work

    def getSalary(self) -> int:
        return self._salary

    def getDictionary(self) -> dict:
        super_dict = super().getDictionary()
        employee_dict = {
            "field_of_work": self._field_of_work,
            "salary": self._salary,
        }
        return super_dict | employee_dict

    def printEmployee(self, num_of_digits: str = "", end: str = "\n") -> None:
        spacer = getSpacer(num_of_digits)

        self.printPerson(num_of_digits, end)
        print(f"{spacer}  Field of Work: {self._field_of_work}")
        print(f"{spacer}  Salary:        {self._salary}", end=end)

    def printMyself(self, num_of_digits: str = "", end: str = "\n"):
        self.printEmployee(num_of_digits, end)
