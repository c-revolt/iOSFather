from aiogram import types
#from aiogram.filters import CommandObject

from bot.commands.bot_commands import bot_commands


async def courses_command(message: types.Message) -> None:
    await message.answer(
        'команда КУРС'
    )
    # if command.args:
    #     for cmd in bot_commands:
    #         if cmd[0] == command.args:
    #             return await message.answer(
    #                 f'{cmd[0]} - {cmd[1]}\n\n{cmd[2]}'
    #             )
    #     else:
    #         return await message.answer('команда не найдена!')
    #
    # return await message.answer(
    #     'Альтернативный вывод\n'
    #     'Почему по курсам выводится эта ветка?\n'
    #)