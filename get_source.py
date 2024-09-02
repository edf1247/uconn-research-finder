from requests_html import HTMLSession
from bs4 import BeautifulSoup

base_url = "https://engineering.uconn.edu/faculty/"

s = HTMLSession()

def load_page(url):
    r = s.get(url=url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

page = load_page(base_url)

with open("source.txt", "w", encoding="utf-8") as f:
    f.write(page.prettify())