from enum import Enum, auto


class Role(Enum):
    COACH = auto()
    JANITOR = auto()
    SOCIAL_WORKER = auto()
    TEACHER = auto()

class Employee():

    name: str
    role: Role