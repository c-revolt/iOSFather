from aiogram import types


async def contacts_command(message: types.Message) -> None:
    await message.answer(
        'Это основной текст меню Контакты'
    )