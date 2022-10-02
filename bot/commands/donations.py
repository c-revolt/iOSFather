from aiogram import types


async def donations_command(message: types.Message) -> None:
    await message.answer(
        'Это основной текст меню Донаты'
    )