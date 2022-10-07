from aiogram import types


async def library_command(message: types.Message) -> None:
    await message.answer(
        '🏛 <b>[ БИБЛИОТЕКА ]</b>\n\n'
        
        '<i>Здесь представлены книги и статьи для более глубокого изучения и понимания программирования.'
        ' Сразу скажу, что ссылки на книги ведут на платные источники,' 
        ' но если хорошо поискать, то можно найти тг-каналы, где их можно скачать бесплатно.</i>\n\n'


        '📓 <a href="https://www.litres.ru/charlz-petcold/kod-taynyy-yazyk-informatiki/">Код. Тайный Язык Информатики</a>'
        ' - это детально иллюстрированная и максимально понятная книга,' 
        ' дающая реальный контекст для понимания современного мира ПК, цифровых медиа и Интернета.\n\n'

        '📓 <a href="https://www.litres.ru/charlz-petcold/kod-taynyy-yazyk-informatiki/">Теоретический Минимум по Computer Science</a>'
        ' - Владстон Феррейра Фило знакомит нас с вычислительным мышлением, позволяющим решать любые сложные задачи.\n\n'

        '📓 <a href="https://www.learnenough.com/command-line-tutorial/basics">Learn Enough Command Line to Be Dangerous</a>'
        ' - это беспланая книга на английском, которая поможет тебе профессионально работать с терминалом.\n\n'

        '📓 <a href="https://www.litres.ru/robert-s-martin/chistaya-arhitektura-iskusstvo-razrabotki-program-39113892/">' 
        'Чистая Архитектура</a>'
        ' - Роберт Мартин дает прямые и лаконичные ответы на ключевые вопросы архитектуры и дизайна.\n\n'

        '🧾 <a href="https://refactoring.guru/ru/design-patterns/swift">Паттерны Проектирования</a>'
        ' - здесь собраны все известные паттерны с описанием и примерами на разных языках, в том числе и на Swift.\n\n'

        '🧾 <a href="http://spacemath.xyz">Математика с 0 для взрослых</a>'
        ' - если хочешь конкретно освоить матан, то этот ресурс пошагово проведёт тебя "из грязи в князи"' 
        ' в этом суровом мире.\n\n'

    )