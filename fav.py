import requests
from bs4 import BeautifulSoup
from datetime import date

def extract_source(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    source=requests.get(url, headers=headers)
    return source

base="https://www.hindustantimes.com/astrology/horoscope"
page = extract_source(base)

soup = BeautifulSoup(page.content, "html.parser")
child_soup = soup.find_all("h3",class_="hdg3")

today=date.today()
d=today.strftime("%B %d")

text = 'Horoscope Today: Astrological prediction for '+d 
new_url=""
for i in child_soup:
    if i.string is not None:
        if text in i.string:
            new_url="https://www.hindustantimes.com"+i.a.get("href")

page = extract_source(new_url)

soup = BeautifulSoup(page.content, "html.parser")
child_soup = soup.find_all("p")

text = 'Lucky Colour:'
li=[]
for i in child_soup:
    if i.string is not None:
        if text in i.string:
            li.append(i.string)

lucky=li[4][14:]
hex_url="https://rgbcolorcode.com/color/"+lucky.lower()
page = extract_source(hex_url)

soup = BeautifulSoup(page.content, "html.parser")
hexcode=soup.title.string[-7:]


print(lucky,hexcode)