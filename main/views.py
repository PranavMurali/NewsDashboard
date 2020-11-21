from django.shortcuts import render
from django.http import HttpResponse
from .models import marks
from django.contrib.auth.decorators import login_required
from main.scrap import deo
# Create your views here.


def home(request):
    context={
        "posts":marks.objects.all(),
        "Title":"Home"
    }
    return render(request,'main/home.html',context)

def about(request):
    return render(request,'main/about.html')

@login_required
def scrap(request):
    context={
        "all":deo.a
    }
    return render(request,'main/scrap.html',context)

def luckyc(request):
    return render(request,'main/luckyc.html')


def luckyd(request):
    return render(request,'main/luckyd.html')