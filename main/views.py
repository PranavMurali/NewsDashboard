from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts=[
    {
        "author":"me",
        "title":"wose",
        "content":"wo",
        "date":"23421"
    },
    {
        "author":"meeses",
        "title":"wosesse",
        "content":"wsesefo",
        "date":"2342sef1"
    }
]
def home(request):
    context={
        "posts":posts,
        "Title":"Home"
    }
    return render(request,'main/home.html',context)

def about(request):
    return render(request,'main/about.html')