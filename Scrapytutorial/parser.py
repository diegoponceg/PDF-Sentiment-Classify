import requests
from bs4 import BeautifulSoup


def parse(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')

    print(html)
