from typing import Union

from tortoise.exceptions import DoesNotExist

from app.db import models


class Messages(models.Messages):
    """
    User model, contains all methods for working with users.
    """
    @classmethod
    async def get_dict(cls, id: int) -> Union[dict, None]:
        """
        Get user by id.
        :param user_id: User id.
        :return: User dict.
        """
        try:
            return await cls.get(id=id)
        except DoesNotExist:
            return None


    @classmethod
    async def create_message(cls, text: str, toxic: float, neutral: float) -> dict:
        """
        Create user.
        :param text: User text.
        :param toxic: User toxic.
        :param neutral: User neutral.
        :return: User dict.
        """
        return await cls.create(text=text, toxic=toxic, neutral=neutral)
    

    @classmethod
    async def get_history(cls) -> list[dict]:
        """
        Get history.
        :return: History.
        """
        return await cls.all()
