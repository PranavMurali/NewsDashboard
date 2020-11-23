from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Marks
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.scrap import scrapnews
from main.anlysis import analysis
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        context={
            "posts":Marks.objects.filter(author=request.user),
            "Title":"Home"
        }
        return render(request,'main/home.html',context)
    else:
        context={
            "posts":Marks.objects.filter(author="2"),
            "Title":"Home"
        }
        return render(request,'main/home.html',context)

def about(request):
    return render(request,'main/about.html')

@login_required
def scrap(request):
    Marks.objects.filter(author=request.user).delete()
    scrapnews(request.user)
    context={
        "all":Marks.objects.filter(author=request.user)
    }
    messages.success(request,f'Latest news has been scraped !')
    return render(request,'main/scrap.html',context)

def luckyc(request):
    return render(request,'main/luckyc.html')

def luckyd(request):
    return render(request,'main/luckyd.html')

def clearfeed(request):
    messages.warning(request, f'Your feed hath been cleansed')
    Marks.objects.filter(author=request.user).delete()
    return redirect("Main-home") 