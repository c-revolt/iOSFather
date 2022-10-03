from aiogram import types


async def simulators_command(message: types.Message) -> None:
    await message.answer(
        '🥊 <b>Тренажеры</b>\n\n'
        
        '🛝 <a href="https://developer.apple.com/swift-playgrounds/">Swift Playgrounds</a>'
        ' - задачи\n\n'
        
        '🏹 <a href="https://leetcode.com">LeetCode</a>'
        ' - задачи\n\n'

        '🏃‍ <a href="https://www.hackingwithswift.com/100">100 Days of Swift</a>'
        ' - марафон по Swift\n\n'

        '🚴‍ <a href="https://www.hackingwithswift.com/100/swiftui">100 Days of SwiftUI</a>'
        ' - марафон по SwiftUI\n\n'

        '📲 <a href="https://apps.apple.com/ru/app/свифти-квиз/id1525844750">Swifty-квиз</a>'
        ' - приложение с вопросами по теории\n\n'

        '🖥 <a href="https://learngitbranching.js.org">GitBranch</a>'
        ' - тренажер по обучению работы в терминале\n\n'

        '🧑‍💻 <a href="https://typerun.top/#rus_basic">Typerun</a>'
        ' - тренажер по обучению слепой печати\n\n'

    )

