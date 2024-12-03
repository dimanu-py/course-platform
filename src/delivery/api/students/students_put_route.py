from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.contexts.backoffice.students.application.create_student_command import (
    CreateStudentCommand,
)
from src.contexts.backoffice.students.application.student_creator import StudentCreator
from src.contexts.backoffice.students.domain.student_repository import StudentRepository
from src.delivery.api.students.student_create_request import CreateStudentRequest

router = APIRouter(prefix="/students", tags=["Students"])


@router.put("/{_id}")
async def create_student(_id: str, request: CreateStudentRequest) -> JSONResponse:
    student_creator = StudentCreator(repository=StudentRepository())
    command = CreateStudentCommand(_id, request.name, request.username, request.email)

    student_creator(command)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={})
