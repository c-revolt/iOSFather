from aiogram import types


async def documentation_command(message: types.Message) -> None:
    await message.answer(
        'Это основной текст меню Документация'
    )

