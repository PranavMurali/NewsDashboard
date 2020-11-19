from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="Main-home"),
    path('about/',views.about,name="Main-about")
]
