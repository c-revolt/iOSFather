__all__ = ['register_user_commands', 'bot_commands']

from aiogram import Router
from aiogram.filters import Command
from bot.commands.start import start
from bot.commands.giude import giude_command
from bot.commands.courses import courses_command
from bot.commands.simulators import simulators_command
from bot.commands.library import library_command
from bot.commands.documentation import documentation_command
from bot.commands.youtube import youtube_command
from bot.commands.mock_interview import mock_command
from bot.commands.tools import tools_command
from bot.commands.useful import useful_command
from bot.commands.donations import donations_command
from bot.commands.contacts import contacts_command

def register_user_commands(router: Router) -> None:
    router.message.register(start, Command(commands=['start']))
    router.message.register(giude_command, Command(commands=['guide']))
    router.message.register(courses_command, Command(commands=['courses']))
    router.message.register(simulators_command, Command(commands=['simulators']))
    router.message.register(library_command, Command(commands=['library']))
    router.message.register(documentation_command, Command(commands=['documentation']))
    router.message.register(youtube_command, Command(commands=['youtube']))
    router.message.register(mock_command, Command(commands=['mock_interview']))
    router.message.register(tools_command, Command(commands=['tools']))
    router.message.register(useful_command, Command(commands=['useful']))
    router.message.register(donations_command, Command(commands=['donations']))
    router.message.register(contacts_command, Command(commands=['contacts']))


