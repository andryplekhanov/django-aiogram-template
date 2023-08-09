from aiogram.dispatcher.filters.state import StatesGroup, State


class UsersStates(StatesGroup):
    """
    Класс реализует состояние пользователя внутри сценария.
    Атрибуты заполняются во время опроса пользователя.

    Attributes:
        last_command (str): команда, которую ввёл пользователь.
    """

    last_command = State()
