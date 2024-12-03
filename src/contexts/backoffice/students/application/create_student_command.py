from dataclasses import dataclass


@dataclass
class CreateStudentCommand:
    id_: str
    name: str
    username: str
    email: str
