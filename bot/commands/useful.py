from aiogram import types


async def useful_command(message: types.Message) -> None:
    await message.answer(
        'Это основной текст меню Полезное'
    )