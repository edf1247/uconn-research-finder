from requests_html import HTMLSession
import bs4
import re
import json

links = []

f = open('prof_links.txt', 'r')
for line in f:
    links.append(line)
f.close()

s = HTMLSession()

def load_page(u):
    r = s.get(url=u)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    return soup


def select_string(element, pattern):
    match = re.search(pattern, str(element))
    if match:
        return match.group(1)


def return_info(soup):
    name = soup.find("h1")
    website = soup.find("td", attrs={"class": "person-url"})
    title = name.find_next_sibling('p')
    department = title.find_next_sibling('p')
    bio = department.find_next_sibling('p')


    w = select_string(website, r'href="([^"]*)"')
    n = select_string(name, r'>\s*(.*?)\s*</')
    t = select_string(title, r'>\s*(.*?)\s*</')
    d = select_string(department, r'>\s*(.*?)\s*</')
    b = select_string(bio, r'>\s*(.*?)\s*</')

    dict = {'prof_name': n, 'prof_site': w, 'prof_title': t, 'prof_department': d, 'prof_bio': b}
    return dict

info_arr = []


for url in links:
    page=load_page(url)
    info_arr.append(return_info(page))

    


with open('professor_info.txt', 'w') as fout:
    json.dump(info_arr, fout)