from bs4 import BeautifulSoup
import requests
from requests.api import request
from .models import Marks
from main.anlysis import analysis
hrefa=[]
title=[]
data=[]

def scrapnews(user): 
    url="https://www.goodnewsnetwork.org/category/news/"
    html_doc=requests.get(url).content
    soup = BeautifulSoup(html_doc, 'html.parser')
    for a in soup.find_all('h3', {'class':'entry-title td-module-title'}):
        title.append(a.text)
    for b in soup.find_all('a', {'rel':'bookmark'}):
        hrefa.append(b['href'])
    href=hrefa[0:len(hrefa):2]
    url="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
    html_doc=requests.get(url).content
    soup = BeautifulSoup(html_doc, 'html.parser')
    for a in soup.find_all('h3', {'class':'ipQwMb ekueJc RD0gLb'}):
        title.append(a.text)
    for b in soup.find_all('a', {'class':'DY5T1d'}):
        href.append("https://news.google.com/"+b['href'])
    scr=analysis(title)
    scrs=list(map(str, scr)) 
    for i in range(len(title)):  
        datas=Marks(content=href[i],author=user,title=title[i],score=scrs[i])
        data.append([title[i],scr[i],href[i]])
        datas.save()
    return data
