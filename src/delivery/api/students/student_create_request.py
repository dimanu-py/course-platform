from dataclasses import dataclass


@dataclass
class CreateStudentRequest:
    name: str
    username: str
    email: str
