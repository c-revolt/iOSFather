from aiogram import types


async def mock_command(message: types.Message) -> None:
    await message.answer(
        'Это основной текст меню Mock-interview'
    )