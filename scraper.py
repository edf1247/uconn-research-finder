import bs4
import re

f = open("source.txt", "r", encoding="utf-8")
soup = bs4.BeautifulSoup(f, "html.parser")
f.close()


links = soup.find_all("a", attrs={"class": "person-permalink"})

for link in links:
    for l in link.findChildren():
        l.extract()

arr = []

for link in links:
    arr.append(str(link))

link_arr = []
pattern = r'href="([^"]*)"'

for link in arr:
    match = re.search(pattern, link)
    if(match):
        link_arr.append(match.group(1))

clean_links = [i for n, i in enumerate(link_arr) if i not in link_arr[:n]]

print(len(clean_links))
