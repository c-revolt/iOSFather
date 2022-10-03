from aiogram import types


async def documentation_command(message: types.Message) -> None:
    await message.answer(
        '🗄<b>[ ДОКУМЕНТАЦИЯ ]</b>\n\n'
        
        '📑 <a href="https://docs.swift.org/swift-book/index.html">Apple Developer Documentation</a>'
        ' - последнюя документация для разработчиков, включая руководства, образцы кода, статьи и справочник по API.\n\n'

        '📑 <a href="https://developer.apple.com/documentation/swift/swift-standard-library">Swift Standard Library</a>'
        ' - стандартная библиотека Swift, инфа о примитивах,' 
        ' типах и распространенных шаблонах программирования Swift\n\n'

        '📑 <a href="https://docs.swift.org/swift-book/index.html">Swift Programming Language</a>'
        ' - документация по базовым возможностям Swift\n\n'

        '📑 <a href="https://developer.apple.com/videos/swift">Video WWDC</a>'
        ' - более 200 видеороликов с конференции этого года.\n\n'

        '📑 <a href="https://developer.apple.com/design/human-interface-guidelines/guidelines/overview/">Human Interface Guidelines</a>'
        ' - HIG содержит рекомендации и передовые практики,' 
        ' которые помогут тебе создать удобный интерфейс для любой платформы Apple.\n\n'
        
        '<B>Фрэймворки</B>\n\n'

        '📑 <a href="https://developer.apple.com/documentation/uikit">UIKit</a>'
        ' - основной фреймворк для создания UI и событий в твоих приложениях.\n\n'

        '📑 <a href="https://developer.apple.com/documentation/swiftui/">SwiftUI</a>'
        ' - декларативный способ создания приложений.\n\n'

        '📑 <a href="https://developer.apple.com/documentation/coreml">Core ML</a>'
        ' - интегрируй модели машинного обучения в свое приложение.\n\n'

        '📑 <a href="https://developer.apple.com/documentation/coreml">Create ML</a>'
        ' - создавай модели машинного обучения для своего приложения.\n\n'

        '📑 <a href="https://developer.apple.com/documentation/arkit/">ARKit</a>'
        ' - создавай дополненую раяльность в своём приложении или игре.\n\n'

        '📑 <a href="https://developer.apple.com/documentation/spritekit/">SpriteKit</a>'
        ' - добавляй 2D контент с плавной анимацией или создай 2D игру.\n\n'

        '📑 <a href="https://developer.apple.com/documentation/metal/">Metal</a>'
        ' - рендеринг расширенной 3D-графики и обработка данных параллельно с графическими процессорами.\n\n'
        
        'Этот список фреймворков далеко не полный. У Apple их ещё очень много,' 
        ' и каждый из них предназначен для разных задач: работа с картами, звуками и прочее.'

    )

