import requests
from bs4 import BeautifulSoup
import re
import csv

url = 'https://en.wikipedia.org/wiki/Wikipedia:Featured_articles'
r = requests.get(url)
start_url = 'https://en.wikipedia.org'
soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find(id= "mw-content-text")
all_headers = table.find_all(re.compile("h[2-4]"))

category = []
name = []
link = []
preview_article = []

for i in range (len(all_headers)):
    for y in range(len(all_headers[i].findNextSibling('ul').findAll('a'))):
        url = start_url + all_headers[i].findNextSibling('ul').findAll('a')[y]['href']
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        content__article = soup.find(id = 'mw-content-text')
        first__p__cont_article = content__article.find('p')
        preview = first__p__cont_article.getText()

        category.append(all_headers[i].getText())
        name.append(all_headers[i].findNextSibling('ul').findAll('a')[y].getText())
        link.append(url)
        preview_article.append(preview)

with open ('ready.csv','w',encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(('category', 'name', 'link', 'preview article'))
    for row in zip(category,name,link,preview_article):
        writer.writerow(row)
