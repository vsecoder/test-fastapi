from fastapi import APIRouter
from app.handlers.messages.api import router as user_router

router = APIRouter()

router.include_router(user_router, prefix="/toxic", tags=["toxic"])


@router.get("/")
async def api_root():
    return {"ping": "pong"}
