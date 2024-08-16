import telebot
from telebot import types
import sqlite3
import datetime
import time
# Замените TOKEN на ваш токен бота
TOKEN = '7410644155:AAHdQ19Wd8rkZ8dy8dNZ1yEhZCtvFrB5sGk'

conn = sqlite3.connect('tasks.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Status
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
              name_of_status TEXT NOT NULL)''')
#c.execute('INSERT INTO Status (name_of_status) VALUES (?)', ("Сделать",))
#c.execute('INSERT INTO Status (name_of_status) VALUES (?)', ("В процессе",))
#c.execute('INSERT INTO Status (name_of_status) VALUES (?)', ("Готово",))



c.execute('''CREATE TABLE IF NOT EXISTS Notification
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              time TEXT NOT NULL)''')
#c.execute('INSERT INTO Notification (time) VALUES (?)', ("None",))


c.execute('''CREATE TABLE IF NOT EXISTS Task
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name_of_task TEXT NOT NULL, 
              status_id INTEGER NOT NULL,
              notification_id INTEGER NOT NULL,
              FOREIGN KEY (status_id) REFERENCES Status(id),
              FOREIGN KEY (notification_id) REFERENCES Notification(id))''')

conn.commit()
c.close()

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
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()

        user_id = message.chat.id
        def reminders(user_id):
            date_time_str = "2024-08-16 23:35"
            date_time = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')

            while True:
                now = datetime.datetime.now()
                if now >= date_time:
                    bot.send_message(chat_id=user_id, text="Напоминание: Пора сделать что-то важное!")
                    break
                time.sleep(1)
        global name_of_task


        if user_id in user_states and user_states[user_id] == 'waiting_for_task':

            name_of_task = message.text
            status_id = 1
            notification_id = 1

            c.execute("INSERT INTO Task (name_of_task, status_id, notification_id) VALUES (?, ?, ?)",
                      (name_of_task, status_id, notification_id))
            del user_states[user_id]
            bot.send_message(chat_id=user_id, text="Дело добавлено. Хотите установить напоминание?")

            user_states[user_id] = 'adding_timer'
        elif user_id in user_states and user_states[user_id] == 'adding_timer':
            if message.text == "да":
                bot.send_message(chat_id=user_id, text="В какое время вам напомнить об этой задаче?")
                del user_states[user_id]
                user_states[user_id] = 'waiting_for_time'
            elif message.text == "нет":
                print("Не добавляем")

                bot.send_message(chat_id=user_id, text="Хорошо, эта задача будет без напоминания")
                del user_states[user_id]
            else:
                bot.send_message(chat_id=user_id, text="На это у меня нет ответа...")
        elif user_id in user_states and user_states[user_id] == 'waiting_for_time':
            notification_time = message.text #"2023-08-16 10:30:00"
            del user_states[user_id]
            c.execute("INSERT INTO Notification (time) VALUES (?)", (notification_time,))
            bot.send_message(chat_id=user_id, text="Напоминание добавлено!")
            c.execute("SELECT id FROM Notification WHERE time = ?", (notification_time,))
            notification_id = c.fetchone()[0]
            c.execute("UPDATE Task SET notification_id = ? WHERE name_of_task = ?",(notification_id, name_of_task))
            print(notification_id)
            print(notification_time)
            reminders(user_id)

        conn.commit()
        conn.close()


@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    if call.data == "button1":
        bot.send_message(chat_id=call.message.chat.id, text="Вы нажали Кнопку 1")
    elif call.data == "button2":
        bot.send_message(chat_id=call.message.chat.id, text="Вы нажали Кнопку 2")
    elif call.data == "button3":
        bot.send_message(chat_id=call.message.chat.id, text="Вы нажали Кнопку 3")


bot.polling(none_stop=True)