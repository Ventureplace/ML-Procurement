from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.title.string
print(f'Title of the website is: {title}')
