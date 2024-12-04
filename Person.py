from utils import getSpacer


class Person:
    def __init__(self, id: int, name: str, age: int) -> None:
        self._id = id
        self._name = name
        self._age = age

    def getID(self) -> int:
        return self._id

    def getName(self) -> str:
        return self._name

    def getAge(self) -> int:
        return self._age

    def getType(self) -> str:
        return self.__class__.__name__

    def getDictionary(self) -> dict:
        return {
            "id": self._id,
            "name": self._name,
            "age": self._age,
        }

    def printPerson(self, num_of_digits: str = "", end: str = "\n") -> None:
        spacer = getSpacer(num_of_digits)

        print(f"{num_of_digits}. Type: {self.getType()}")
        print(f"{spacer}  Name: {self._name}")
        print(f"{spacer}  ID:   {self._id}")
        print(f"{spacer}  Age:  {self._age}", end=end)

    def printMyself(self, num_of_digits: str = "", end: str = "\n") -> None:
        self.printPerson(num_of_digits, end)
