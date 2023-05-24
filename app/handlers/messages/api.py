from fastapi import APIRouter

from app.db.functions import Messages
from app.utils.api import API

router = APIRouter()
api = API()


@router.get("/")
async def check_text(text: str):
    """
    Check text.
    :param text: Text.
    :return: Text.
    """
    answer = api.check(text)
    await Messages.create_message(text=text, toxic=answer["toxic_percent"], neutral=answer["neutral_percent"])
    return answer


@router.get("/history")
async def get_history():
    """
    Get history.
    :return: History.
    """
    return await Messages.get_history()