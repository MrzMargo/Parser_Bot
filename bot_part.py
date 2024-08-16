import telebot
from telebot import types
# Замените TOKEN на ваш токен бота
TOKEN = '7410644155:AAHdQ19Wd8rkZ8dy8dNZ1yEhZCtvFrB5sGk'

"""# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Команда "/start"
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Кнопка 1")
    item2 = types.KeyboardButton("Кнопка 2")
    markup.add(item1, item2)

    bot.send_message(chat_id=message.chat.id, text="Привет! Выберите одну из кнопок:", reply_markup=markup)

# Обработчик для кнопок
@bot.message_handler(content_types=['text'])
def button_handler(message):
    if message.text == "Кнопка 1":
        bot.send_message(chat_id=message.chat.id, text="Вы нажали Кнопку 1")
    elif message.text == "Кнопка 2":
        bot.send_message(chat_id=message.chat.id, text="Вы нажали Кнопку 2")
    else:
        bot.send_message(chat_id=message.chat.id, text="Привет, мир!")

# Запуск бота
bot.polling(none_stop=True)"""
"""# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Команда "/start"
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем клавиатуру с кнопками
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Кнопка 1", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Кнопка 2", callback_data="button2")
    keyboard.add(button1, button2)

    # Отправляем сообщение с клавиатурой
    bot.send_message(chat_id=message.chat.id, text="Привет! Выберите одну из кнопок:", reply_markup=keyboard)

# Обработчик для нажатия кнопок
@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    if call.data == "button1":
        bot.send_message(chat_id=call.message.chat.id, text="Вы нажали Кнопку 1")
    elif call.data == "button2":
        bot.send_message(chat_id=call.message.chat.id, text="Вы нажали Кнопку 2")

# Запуск бота
bot.polling(none_stop=True)"""

bot = telebot.TeleBot(TOKEN)
user_states = {}
# Команда "/start"
@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Добавить задачу", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Посмотреть задачи", callback_data="button2")
    button3 = types.InlineKeyboardButton(text="Что ты умеешь?", callback_data="button3")
    keyboard.add(button1, button2, button3)
    bot.send_message(chat_id=message.chat.id, text="Привет! Я помогу организовать ваш день!", reply_markup=keyboard)
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(chat_id=user_id, text="Вам нужна помощь? Вот, что я могу:...")

@bot.message_handler(commands=['newtask'])
def send_welcome(message):
    user_id = message.chat.id
    user_states[user_id] = 'waiting_for_task'
    bot.send_message(chat_id=user_id, text="Отлично! Какой будет задача?")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
        user_id = message.chat.id
        if user_id in user_states and user_states[user_id] == 'waiting_for_task':
            task_text = message.text
            print(f"Новое дело: {task_text}")
            with open("user_messages.txt", "a") as file:
                for user_id, message in data.items():
                    file.write(f"User ID: {user_id}, Message: {message}\n")

            del user_states[user_id]
            bot.send_message(chat_id=user_id, text="Дело добавлено. Хотите установить напоминание?")
            user_states[user_id] = 'adding_timer'
        elif user_id in user_states and user_states[user_id] == 'adding_timer':
            if message.text == "да":
                print("Добавляем таймер")
                bot.send_message(chat_id=user_id, text="Напоминание установлено!")
                del user_states[user_id]
            elif message.text == "нет":
                print("Не добавляем")
                bot.send_message(chat_id=user_id, text="Хорошо, эта задача будет без напоминания")
                del user_states[user_id]
            else:
                bot.send_message(chat_id=user_id, text="На это у меня нет ответа...")


@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    if call.data == "button1":
        bot.send_message(chat_id=call.message.chat.id, text="Вы нажали Кнопку 1")
    elif call.data == "button2":
        bot.send_message(chat_id=call.message.chat.id, text="Вы нажали Кнопку 2")
    elif call.data == "button3":
        bot.send_message(chat_id=call.message.chat.id, text="Вы нажали Кнопку 3")

bot.polling(none_stop=True)