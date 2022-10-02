from aiogram import types


async def tools_command(message: types.Message) -> None:
    await message.answer(
        'Это основной текст меню Инструменты'
    )