# Python course - level 3 - Advanced
# Lesson 66 - Final Project - Revision 1
# Author: Rephael Sintes

import pandas as pd
from options import MenuOptions, PersonOptions
from utils import isDigit
from Person import Person
from Student import Student
from Employee import Employee


def printMenu():
    for menu_option in MenuOptions:
        print(f"{menu_option.value}. {menu_option.name}")


def saveNewEntry(entries_lst: list, ids_dict: dict) -> int:
    entry_type = input("Type of entry: 1. Person, 2. Student, 3. Employee: ")
    while entry_type not in ["1", "2", "3"]:
        entry_type = input("Type of entry: 1. Person, 2. Student, 3. Employee: ")
    entry_type = PersonOptions(int(entry_type))

    id_number = input("ID: ")
    if isDigit(id_number, "ID"):
        id_number = int(id_number)
    else:
        return 0
    if id_number in ids_dict:
        existing_entry = entries[ids_dict[id_number]]
        existing_name = f"'name': '{existing_entry.getName()}'"
        existing_age = f"'age': {existing_entry.getAge()}"
        print(f"Error: ID already exists: {{{existing_name}, {existing_age}}}")
        return 0

    name = input("Name: ")
    if not name.isalpha():
        print(
            f"Error: Name must contain only alphabetical characters. {name} is not alphabetical"
        )
        return 0

    age = input("Age: ")
    if isDigit(age, "Age"):
        age = int(age)
    else:
        return 0

    functions_map = {
        PersonOptions.PERSON: Person,
        PersonOptions.STUDENT: Student,
        PersonOptions.EMPLOYEE: Employee,
    }

    entries_lst.append(functions_map[entry_type](id_number, name, age))

    ids_dict[id_number] = len(entries_lst) - 1
    print(f"ID [{id_number}] saved successfully")
    return age


def searchByID(entries_lst: list) -> None:
    id_to_search = input("Please enter the ID you want to look for: ")
    if isDigit(id_to_search, "ID"):
        id_to_search = int(id_to_search)
    else:
        return

    if id_to_search not in ids_to_indices:
        print(f"Error: ID {id_to_search} is not saved")
        return

    index = ids_to_indices[id_to_search]
    printEntryData(index, entries_lst[index])


def printAgesAverage(entries_num: int, ages_sum_value: int) -> None:
    if entries_num == 0:
        print(0.0)
    else:
        print(ages_sum_value / entries_num)


def printAllNames(entries_lst: list) -> None:
    for index, person in enumerate(entries_lst):
        print(f"{index}. {person.getName()}")


def printAllIDs(entries_lst: list) -> None:
    for index, person in enumerate(entries_lst):
        print(f"{index}. {person.getID()}")


def printAllEntries() -> None:
    for index, person in enumerate(entries):
        printEntryData(index, person, "\n\n")


def printEntryByIndex(last_index: int, entries_lst: list) -> None:
    index_to_print = input("Please enter the index of the entry you want to print: ")
    if isDigit(index_to_print, "Index"):
        index_to_print = int(index_to_print)
    else:
        return

    if index_to_print > last_index:
        print(f"Error: Index out of range. The maximum index allowed is {last_index}")
        return

    printEntryData(index_to_print, entries_lst[index_to_print])


def saveAllData(entries_lst: list) -> None:
    output_file_name = input("What is your output file name? ")
    dicts_lst = [entry.getDictionary() for entry in entries_lst]
    df = pd.DataFrame(dicts_lst)
    df.to_csv(output_file_name, index=False)


def exitProgram() -> None:
    to_exit = input("Are you sure? (y/n)")
    while to_exit not in ["y", "n"]:
        to_exit = input("Are you sure? (y/n)")
    if to_exit == "y":
        exit(0)


def printEntryData(index: int, person: Person, end: str = "\n") -> None:
    person.printMyself(str(index), end)


def homeScreen(entries_lst: list, ids_dict: dict) -> None:
    try:
        global ages_sum
        printMenu()
        option = input("Please enter your option:")

        try:
            option = MenuOptions(int(option))
        except ValueError:
            print(f"Error: Option {option} does not exist. Please try again")
            return

        functions_map = {
            MenuOptions.SAVE_A_NEW_ENTRY: lambda: saveNewEntry(entries_lst, ids_dict),
            MenuOptions.SEARCH_BY_ID: lambda: searchByID(entries_lst),
            MenuOptions.PRINT_AGES_AVERAGE: lambda: printAgesAverage(
                len(entries_lst), ages_sum
            ),
            MenuOptions.PRINT_ALL_NAMES: lambda: printAllNames(entries_lst),
            MenuOptions.PRINT_ALL_IDS: lambda: printAllIDs(entries_lst),
            MenuOptions.PRINT_ALL_ENTRIES: lambda: printAllEntries(),
            MenuOptions.PRINT_ENTRY_BY_INDEX: lambda: printEntryByIndex(
                len(entries_lst) - 1, entries_lst
            ),
            MenuOptions.SAVE_ALL_DATA: lambda: saveAllData(entries_lst),
            MenuOptions.EXIT: lambda: exitProgram(),
        }

        result = functions_map[option]()
        if option == MenuOptions.SAVE_A_NEW_ENTRY:
            ages_sum += result

        input("Press enter to continue")
    except Exception as e:
        print(e)


entries = []
ids_to_indices = {}
ages_sum = 0

entries.append(Person(101, "Rephael", 27))
entries.append(Person(102, "Nadav", 36))
entries.append(Person(103, "Sapir", 24))
entries.append(Person(104, "Jane", 21))
entries.append(Person(105, "Goliath", 32))
entries.append(Person(106, "David", 70))
entries.append(Person(107, "Trump", 72))
entries.append(Student(108, "Alex", 29, "Math", 2, 89))
entries.append(Student(109, "James", 31, "Physics", 3, 79))
entries.append(Employee(110, "Galit", 42, "Dentist", 32000))
entries.append(Employee(111, "Sean", 39, "Register", 7500))
entries.append(Employee(111, "Alma", 27, "Doctor", 14500))
entries.append(Employee(111, "Judah", 44, "King", 8150000))
entries.append(Employee(111, "Hilah", 18, "Cashier", 5800))

ids_to_indices[101] = 0
ids_to_indices[102] = 1
ids_to_indices[103] = 2
ids_to_indices[104] = 3
ids_to_indices[105] = 4
ids_to_indices[106] = 5
ids_to_indices[107] = 6
ids_to_indices[108] = 7
ids_to_indices[109] = 8
ids_to_indices[110] = 9
ids_to_indices[111] = 10
ids_to_indices[112] = 11
ids_to_indices[113] = 12
ids_to_indices[114] = 13


ages_sum += 27
ages_sum += 36
ages_sum += 24
ages_sum += 21
ages_sum += 32
ages_sum += 70
ages_sum += 72
ages_sum += 29
ages_sum += 31
ages_sum += 41
ages_sum += 39
ages_sum += 27
ages_sum += 44
ages_sum += 18

while True:
    homeScreen(entries, ids_to_indices)
