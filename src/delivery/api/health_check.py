from fastapi import APIRouter, status
from fastapi.responses import JSONResponse


router = APIRouter(tags=["Health Check"])


@router.get("/health-check")
async def health_check() -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "Healthy"})
