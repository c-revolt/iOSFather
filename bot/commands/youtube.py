from aiogram import types


async def youtube_command(message: types.Message) -> None:
    await message.answer(
        'Это основной текст меню YouTube'
    )