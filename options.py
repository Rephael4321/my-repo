from enum import Enum, auto


class MenuOptions(Enum):
    SAVE_A_NEW_ENTRY = auto()
    SEARCH_BY_ID = auto()
    PRINT_AGES_AVERAGE = auto()
    PRINT_ALL_NAMES = auto()
    PRINT_ALL_IDS = auto()
    PRINT_ALL_ENTRIES = auto()
    PRINT_ENTRY_BY_INDEX = auto()
    SAVE_ALL_DATA = auto()
    EXIT = auto()


class PersonOptions(Enum):
    PERSON = auto()
    STUDENT = auto()
    EMPLOYEE = auto()
