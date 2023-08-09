from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.models.commands import add_or_create_user


async def user_start(message: Message, state: FSMContext):
    await state.finish()
    async with state.proxy() as data:
        data['last_command'] = 'start'

    user = await add_or_create_user(user_id=int(message.from_user.id))
    await message.answer(f'Привет. Вы в базе с id {user.tg_id}')

    states = await state.get_data()
    await message.answer(f"вы ввели команду, {states.get('last_command')}")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
