from bs4 import BeautifulSoup
import requests
from requests.api import request
from .models import Marks
from main.anlysis import analysis
hrefa=[]
title=[]

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
    for i in range(len(title)):  
        datas=Marks(content=href[i],author=user,title=title[i],score=scr[i])
        datas.save()
        datas.objects.filter(author=request.user).update(score=scr[i])
