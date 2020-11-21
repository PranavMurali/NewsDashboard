from django.shortcuts import render
from django.http import HttpResponse
from .models import marks
# Create your views here.

def home(request):
    context={
        "posts":marks.objects.all(),
        "Title":"Home"
    }
    return render(request,'main/home.html',context)

def about(request):
    return render(request,'main/about.html')