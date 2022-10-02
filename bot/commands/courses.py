from aiogram import types
#from aiogram.filters import CommandObject

from bot.commands.bot_commands import bot_commands


async def courses_command(message: types.Message) -> None:
    await message.answer(

        '📙 <b>Основы + UIKit</b>\n\n'
        '📖 <a href="https://developer.apple.com/swift-playgrounds/">Learn to code with Swift Playgrounds</a>'
        ' - отличный тренажёр для старта.\n\n'
        
        '📖 <a href="https://developer.apple.com/learn/curriculum/">Develop in Swift</a>'
        ' - курс из трёх полноценных учебников по основам и UIKit.\n\n'
        
        '📖 <a href="https://developer.apple.com/tutorials/app-dev-training/getting-started-with-today">UIKit App</a>'
        ' - курс по основному фреймворку UIKit, который тебе нужно обязательно знать.\n\n'
        
        '📘 <b>SwiftUI</b>\n\n'
        '📖 <a href="https://developer.apple.com/tutorials/SwiftUI">Introducing SwiftUI</a>'
        ' - основы SwiftUI в процессе создания приложения.\n\n'
        
        '📖 <a href="https://developer.apple.com/tutorials/swiftui-concepts">Learning SwiftUI</a>'
        ' - методы создания мультиплатформенных приложений.\n\n'
        
        '📖 <a href="https://developer.apple.com/tutorials/Sample-Apps">Exploring SwiftUI SampleApps</a>'
        ' - определение пользовательских интерфейсов, реагирование на пользователя, управление потоком данных.\n\n'
        
        '📖 <a href="https://developer.apple.com/tutorials/app-dev-training/getting-started-with-scrumdinger">SwiftUI App</a>'
        ' - полнофункциональное приложение.\n\n'

        '📖 <a href="https://www.youtube.com/playlist?list=PLpGHT1n4-mAsxuRxVPv7kj4-dQYoC3VVu">CS193P</a>'
        ' - курс от Stanford.\n\n'
        
        
        '📕 <b>Objective-C</b>\n\n'
        '📖 <a href="https://ru.hexlet.io/courses/objective_c">Objective C и разработка под Mac OS X</a>'
        ' - курс от Hexlet.\n\n'
        
        '📗 <b>Курсы от IT-компаний</b>\n\n'
        'Некоторые крупные IT-компании предлагают свои бесплатные курсы.'
        ' Однако, на них следует записываться если у тебя уже есть какие-то знания.\n\n'
        
        '📖 <a href="https://21-school.ru">Школа 21</a>'
        ' - оффлайн обучение от Sber в школе по типу известной французской Школы 42.\n\n'

        '📖 <a href="https://sbergraduate.ru/ios-school/">iOS Школа</a>'
        ' - курс от Sber Graduate.\n\n'

        '📖 <a href="https://fintech.tinkoff.ru/study/fintech/ios/">iOS-разработчик</a>'
        ' - курс от Tinkoff.\n\n'

        '📖 <a href="https://route256.ozon.ru/ios">Продвинутая iOS-разработка: SwiftUI и Backend Driven UI</a>'
        ' - курс от OzonTech.\n\n'

        '📖 <a href="https://education.vk.company/curriculum/program/discipline/1238/">Разработка приложений на iOS</a>'
        ' - курс от VK.\n\n'




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