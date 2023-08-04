from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.models.commands import add_user


async def user_start(message: Message):
    user = await add_user(message.from_user.id, message.from_user.full_name, message.from_user.username)
    await message.answer(f'hello, {user.username}')


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
