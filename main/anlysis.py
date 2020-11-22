import requests
from requests.api import request
from nltk.sentiment.vader import SentimentIntensityAnalyzer

scr=[]
def analysis(sentence):
    for i in sentence:
        sid = SentimentIntensityAnalyzer()
        scr.append(sid.polarity_scores(i)['compound'])
    return scr
