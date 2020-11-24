from bs4 import BeautifulSoup
import requests
from requests.api import request
from .models import Marks
from main.anlysis import analysis
hrefa=[]
title=[]
data=[]
dicts={}
fintit=[]
finhref=[]
finscr=[]

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
        dic={scr[i]:[title[i],href[i]]}
        dicts.update(dic)
    dictss=dicts.items()
    fin=sorted(dictss,reverse=True)
    for i in range(len(fin)):
        scrs,lists=fin[i]
        fintit.append(lists[0])
        finhref.append(lists[1])
        finscr.append(scrs)
    scrs=list(map(str,finscr)) 
    for i in range(len(fintit)):  
        datas=Marks(content=finhref[i],author=user,title=fintit[i],score=finscr[i])
        data.append([fintit[i],finscr[i],finhref[i],user,datas.date_modified])
        datas.save()
        print(fintit)
        print(finhref)
        print(finscr)
    return data
