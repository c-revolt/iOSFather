from aiogram import types


async def simulators_command(message: types.Message) -> None:
    await message.answer(
        'Это основной текст меню Тренажеры'
    )

