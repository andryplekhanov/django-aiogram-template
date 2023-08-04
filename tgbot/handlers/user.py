from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.models.commands import add_user


async def user_start(message: Message):
    await message.answer('hello')
    user = await add_user(message.from_user.id, message.from_user.full_name, message.from_user.username)
    if user:
        await message.answer('hello')
    else:
        await message.answer('wtf')


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
