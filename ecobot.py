import telebot
from logic_ai import get_class
from confic import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton('🌍 Связь глобального потепления с переработкой мусора', callback_data='global_warming'),
        telebot.types.InlineKeyboardButton('♻️ Переработка разных типов мусора', callback_data='recycling')
    )
    markup.add(telebot.types.InlineKeyboardButton('📷 Определить тип мусора по фото', callback_data='upload_photo'))
    
    bot.send_message(message.chat.id, 'Привет! Я экобот! ♻️')
    bot.send_message(message.chat.id, 'Загрязнение нашей планеты - очень недооценённая проблема. Она помимо неудобства для людей вызывает большие экологические проблемы, спосопствует изменению климата, а также вредно экосистеме Земли')
    bot.send_message(message.chat.id, 'Этот бот посвящён переработке мусора. Выберите, какую функцию бота вы хотите использовать.')
    bot.send_message(message.chat.id, 'После пользования нашим ботом, опишите свои впечатления в письме нам на почту: kumetsanton@gmail.com. Мы будем ждать! ☺️', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'global_warming':
        send_warming(call.message)
    elif call.data == 'recycling':
        send_recycling(call.message)
    elif call.data == 'upload_photo':
        bot.send_message(call.message.chat.id, 'Если ты не знаешь, какой тип мусора перед тобой, загружай фото, чтобы по нему определить тип переробатываемого мусора. Есть 4 класса: макулатура, батарейки, пластиковые бутылки, стекло. Если фотографий несколько, загружай их по одной. Программа может медленно работать, подождите!')


@bot.message_handler(commands=['global_warming'])
def send_warming(message):
    bot.send_message(message.chat.id, 'Глобальное потепление — это повышение средней температуры на планете в течение длительного периода.')
    bot.send_message(message.chat.id, 'Глобальное потепление и сортировка мусора связаны через снижение выбросов парниковых газов:')
    bot.send_message(message.chat.id, 'Сокращение свалок. Органический мусор на свалках разлагается без кислорода, выделяя метан (в 25 раз опаснее CO₂ для климата). Сортировка позволяет перерабатывать или компостировать отходы, уменьшая их объём.')
    bot.send_message(message.chat.id, 'Экономия ресурсов. Переработка (стекла, пластика, металла) требует меньше энергии, чем производство нового сырья → снижаются выбросы CO₂ от заводов.')
    bot.send_message(message.chat.id, 'Меньше мусоросжигания. Сжигание непереработанного мусора выбрасывает CO₂ и токсины. Сортировка сокращает объём отходов для сжигания.')
    bot.send_message(message.chat.id, 'Итог: Сортировка мусора — простой способ замедлить потепление через сокращение метана и CO₂. ♻️🌍')


@bot.message_handler(content_types=['photo'])
def send_class(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    print(file_info)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    result = get_class(file_name)
    bot.send_message(message.chat.id, result)
    if result == 'Макулатура':
            bot.send_message(message.chat.id, 'Напиши команду /paper, и ты узнаешь план сдачи бумаги на переработку')
    if result == 'Батарейки':
            bot.send_message(message.chat.id, 'Напиши команду /batteries, и ты узнаешь план сдачи батареек на переработку')
    if result == 'Пластик':
                bot.send_message(message.chat.id, 'Напиши команду /plastic, и ты узнаешь план сдачи пластика на переработку')
    if result == 'Стекло':
            bot.send_message(message.chat.id, 'Напиши команду /glass, и ты узнаешь план сдачи стекла на переработку')
    bot.send_message(message.chat.id, 'В случае, если перерабатываемый мусор был определён некорректно, опишите вашу проблему в письме, отправленном на почту kumetsanton@gmail.com, и мы обязательно решим вашу проблему.')


@bot.message_handler(commands=['paper'])
def send_paper(message):
    bot.send_message(message.chat.id, 'Для начала надо собрать все имеющиеся бумажные отходы — старые книги, тетради, журналы, газеты, картонные коробки, папки и другие')
    bot.send_message(message.chat.id, 'Не забудь отделить бумагу от картона')
    bot.send_message(message.chat.id, 'Рассортируй отходы по цветам (чёрно-белые отдельно от цветных)')
    bot.send_message(message.chat.id, 'Рассортируй по видам. Разложи по стопкам книги, журналы, газеты, документы, тетради. Стопки с бумажным мусором должны быть однородными')
    bot.send_message(message.chat.id, 'Обязательно убери скрепки, кнопки, файлы, плёнку, скотч!')
    bot.send_message(message.chat.id, 'Для удобной транспортировки и складирования в пункте приёма обвяжи стопки верёвками или сложи в закрывающиеся коробки или пакеты')
    bot.send_message(message.chat.id, 'Теперь доставь их на пункт приёма макулатуры и сдай их. Всё, ты молодец и защитник природы!❤️')

@bot.message_handler(commands=['batteries'])
def send_batteries(message):
    bot.send_message(message.chat.id, 'Правильный способ сортировки батареек заключается в разделении их по химическим типам. Это нужно, чтобы выбрать правильный метод переработки для каждого типа.')
    bot.send_message(message.chat.id, 'В домашних условиях батарейки желательно хранить в герметичной ёмкости с закрытой крышкой.')
    bot.send_message(message.chat.id, 'Сдавать на переработку нужно все батарейки — независимо от названия и состава. Многие крупные магазины устанавливают у себя контейнеры для сбора батареек и оплачивают расходы по их доставке на заводы.')
    bot.send_message(message.chat.id, 'Также боксы для сбора батареек встречаются в подъездах жилых домов, офисах и коворкингах. ')

@bot.message_handler(commands=['plastic'])
def send_plastic(message):
    bot.send_message(message.chat.id, 'Выбери место для сбора пластиков. Это может быть отдельный контейнер или несколько, которые будут стоять в определённом месте дома или офиса, где обычно складывают мусор.')
    bot.send_message(message.chat.id, 'Убедись, что ёмкости для мусора имеют чёткую маркировку о переработке, соответствующую каждому виду пластика. Например, они могут быть подписаны с помощью наклеек или специальных маркеров.')
    bot.send_message(message.chat.id, 'Проверь, чтобы каждый контейнер был чистым и сухим. Это позволит избежать загрязнения пластмассы и обеспечит её качественную переработку.')
    bot.send_message(message.chat.id, 'Если есть возможность, раздели отходы на более мелкие категории. Например, можно отдельно собирать бутылки, пакеты, игрушки и т. д.')
    bot.send_message(message.chat.id, 'Помести каждый пластиковый предмет в соответствующий контейнер для мусора. Если отходы отсортированы на несколько категорий, то каждую категорию нужно поместить в отдельный контейнер для мусора')
    bot.send_message(message.chat.id, 'Перед сдачей отсортированного пластика стоит уточнить в пункте приёма, какие виды пластика принимаются.')
    bot.send_message(message.chat.id, 'После того как контейнеры заполнятся, отнеси их в пункты приёма или на специальные акции по сбору пластиковых отходов.')

@bot.message_handler(commands=['glass'])
def send_glass(message):
    bot.send_message(message.chat.id, 'Определи, какое стекло можно сдать. Подойдут бутылки от напитков, банки из-под консервов или детского питания, а также различные пузырьки. Можно сдать листовое стекло, которое осталось при замене окон.')
    bot.send_message(message.chat.id, 'Подготовь стекло к сдаче. Его нужно ополоснуть от остатков содержимого и снять с тары крышку. Этикетку отрывать не нужно.')
    bot.send_message(message.chat.id, 'Найди пункт приёма стеклотары. В разных городах России есть такие пункты, а также контейнеры для вторсырья (обычно синего цвета).')
    bot.send_message(message.chat.id, 'Сдай стекло в пункт приёма. Вместе со стеклом нельзя сдавать керамическую и стеклянную посуду, очки или линзы, автомобильное стекло, крышки от сковородок и кастрюль, лампочки, зеркала и хрусталь.')

@bot.message_handler(commands=['recycling'])
def send_recycling(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    items = ['Бумага', 'Батарейки', 'Пластик', 'Стекло']
    markup.add(*items)
    bot.send_message(message.chat.id, 'Выбери тип мусора, чтобы узнать план его переработки', reply_markup=markup)

# Обработка выбора
@bot.message_handler(func=lambda msg: msg.text in ['Бумага', 'Батарейки', 'Пластик', 'Стекло'])
def handle_recycling_choice(message):
    if message.text == 'Бумага':
        send_paper(message)
    elif message.text == 'Батарейки':
        send_batteries(message)
    elif message.text == 'Пластик':
        send_plastic(message)
    elif message.text == 'Стекло':
        send_glass(message)

bot.delete_webhook()
bot.infinity_polling()