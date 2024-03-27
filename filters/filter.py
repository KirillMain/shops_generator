from typing import List

from aiogram.filters import BaseFilter
from aiogram.types import Message

from config_reader import config

class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        # if isinstance(self.user_ids, int):
        #     return message.from_user.id == self.user_ids
        # return message.from_user.id in self.user_ids
        return config.admin_id == message.from_user.id