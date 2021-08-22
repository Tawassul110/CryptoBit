from django.shortcuts import render
from .models import News

# Create your views here.
def get_news():

    news = News.objects.all()
    return news