import bs4

f = open("source.txt", "r", encoding="utf-8")
soup = bs4.BeautifulSoup(f, "html.parser")
f.close()


