from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class CreateStudentCommand:
    id_: str
    name: str
    username: str
    email: str
