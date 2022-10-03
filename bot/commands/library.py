from aiogram import types


async def library_command(message: types.Message) -> None:
    await message.answer(
        '🏛 <b>[ БИБЛИОТЕКА ]</b>'
        
        ''
    )