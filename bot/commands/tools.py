from aiogram import types


async def tools_command(message: types.Message) -> None:
    await message.answer(
        '🧰 <b>[ ИНСТРУМЕНТЫ ]</b>\n\n'

        '🔨 <a href="https://developer.apple.com/xcode/">Xcode</a>'
        ' - главная среда разработки для iOS разработчика.\n\n'

        '🔨 <a href="https://developer.apple.com/sf-symbols/">SF Symbols</a>'
        ' - набор иконок от Apple.\n\n'

        '🔨 <a href="https://developer.apple.com/augmented-reality/tools/">AR Creation Tools</a>'
        ' - набор инструментов от Apple для работы с приложениями дополненной реальности.\n\n'

        '🔨 <a href="https://developer.apple.com/machine-learning/models/">Core ML Models</a>'
        ' - набор готовых ML моделей.\n\n'

        '🔨 <a href="https://www.flaticon.com/ru/">Flaticon</a>'
        ' - большой банк с бесплатными иконками для приложений.\n\n'

        '🔨 <a href="https://www.remove.bg/upload">Remove</a>'
        ' - обезать задний фон на фото.\n\n'

        '🔨 <a href="https://appicon.co">Appicon</a>'
        ' - генерирует все размеры иконок. \n\n'

        '🔨 <a href="https://colorhunt.co">Color Hunt</a>'
        ' - наборы цветовых палитр, сочетания цветов. \n\n'

        '🔨 <a href="https://quicktype.io">QuickType</a>'
        ' - преобразование JSON-файлов, можно отловить ошибки.\n\n'

        '🔨 <a href="https://mockuphone.com">MockUphone</a>'
        ' - скриншот приложения можно вставить в рамку iPhone, iPad, MackBook.\n\n'

        '🔨 <a href="https://dribbble.com/shots">Dribble</a>'
        ' - большая база шаблонов готовых приложений от дизайнеров.\n\n'

        '🔨 <a href="https://www.behance.net">Behance</a>'
        ' - ещё одна известная база с шаблонами.\n\n'

        '<b>API</b>\n\n'

        '🔌 <a href="https://unsplash.com">Unsplash</a>'
        ' - большой фотобанк из которого можно подгружать фото в своё приложение.\n\n'
        
        '🔌 <a href="https://www.themoviedb.org/?language=ru">TMDB</a>'
        ' - ресурс, на котором находится куча фильмов с рейтингами и описанием.\n\n'

        '🔌 <a href="https://developer.apple.com/documentation/applemusicapi/">Apple Music API</a>'
        ' - ресурс от Apple для подгрузки музыки в приложение.\n\n'

    )