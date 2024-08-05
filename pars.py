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