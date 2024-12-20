from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from src.contexts.platform.shared.infra.persistence.sqlalchemy.session_maker import (
    SessionMaker,
)
from src.contexts.platform.students.application.create.create_student_command import (
    CreateStudentCommand,
)
from src.contexts.platform.students.application.create.student_creator import (
    StudentCreator,
)
from src.contexts.platform.students.infra.persistence.postgres_student_repository import (
    PostgresStudentRepository,
)
from src.delivery.api.dependency_provider import session_maker_provider
from src.delivery.api.students.student_create_request import (
    CreateStudentRequest,
)

router = APIRouter(prefix="/students", tags=["Students"])


async def creator_provider(
    session_maker: SessionMaker = Depends(session_maker_provider),
) -> StudentCreator:
    session_maker.create_tables()
    repository = PostgresStudentRepository(session_maker=session_maker)
    return StudentCreator(repository=repository)


@router.put("/{id_}")
async def create_student(
    id_: str,
    request: CreateStudentRequest,
    influencer_creator: StudentCreator = Depends(creator_provider),
) -> JSONResponse:
    command = CreateStudentCommand(
        id_=id_, name=request.name, username=request.username, email=request.email
    )

    influencer_creator(command)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={})
