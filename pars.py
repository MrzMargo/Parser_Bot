import requests
from bs4 import BeautifulSoup
import pprint
"""# URL страницы для парсинга
url = "https://ram.by/computers.html"

# Отправляем GET-запрос и получаем HTML-код страницы
response = requests.get(url)
html_content = response.content

# Создаем объект BeautifulSoup для разбора HTML-кода
soup = BeautifulSoup(html_content, "html.parser")

# Находим все заголовки статей на странице
article_titles = soup.find_all("div", class_="items list-view")
#print(article_titles)
pretty_html = soup.prettify()
print(pretty_html)"""

"""params = {'q': 'python'}
response = requests.get('https://api.github.com/search/repositories', params=params)

response_json = response.json()
print(response_json['total_count'])"""




"""
import requests
from bs4 import BeautifulSoup
import telebot

# Replace with your bot token
BOT_TOKEN = '7410644155:AAHdQ19Wd8rkZ8dy8dNZ1yEhZCtvFrB5sGk'

# Create a bot instance
bot = telebot.TeleBot(BOT_TOKEN)

# URL of the page to be parsed
url = "https://5element.by/"

# Function to handle the /start command
@bot.message_handler(commands=['start'])
def start_command(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    btn1 = telebot.types.KeyboardButton("Let's find something new")
    markup.add(btn1)
    bot.reply_to(message, "Hello! Click the 'Parse Website' button to start.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Let's find something new")
def parse_website(message):
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

    article_titles = soup.find_all("div", class_="carousel-slider swiper-container-initialized swiper-container-horizontal")

    pretty_html = soup.prettify()
    print(pretty_html)

# Start the bot
bot.polling()

"""