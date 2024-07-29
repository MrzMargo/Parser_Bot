import requests
from bs4 import BeautifulSoup
import telebot

# Replace with your bot token
BOT_TOKEN = 'YOUR_TOKEN'

# Create a bot instance
bot = telebot.TeleBot(BOT_TOKEN)

# URL of the page to be parsed
url = "https://ram.by/computers.html"

# Function to handle the /start command
@bot.message_handler(commands=['start'])
def start_command(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    btn1 = telebot.types.KeyboardButton('Parse Website')
    markup.add(btn1)
    bot.reply_to(message, "Hello! Click the 'Parse Website' button to start.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Parse Website')
def parse_website(message):
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

    article_titles = soup.find_all("div", class_="items list-view")

    pretty_html = soup.prettify()
    with open('example.txt', 'w', encoding='utf-8') as file:
        for i in pretty_html:
            file.write(i)

    with open('example.txt', 'rb') as file:
        bot.send_document(chat_id=message.chat.id, document=file)
    print(pretty_html)

# Start the bot
bot.polling()