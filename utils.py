def isDigit(num_value: int, num_name: str) -> bool:
    print("bye 222")
    print("hello")
    if num_value.isdigit():
        return True
    print(f"Error: {num_name} must be a number. {num_value} is not a number")
    return False


def getNumberFromUser(subject: str) -> int:
    while True:
        value = input(f"{subject}: ")
        if isDigit(value, subject):
            return int(value)


def getSpacer(num_of_digits: str) -> str:
    return len(num_of_digits) * " "
