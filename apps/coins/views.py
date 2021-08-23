from django.shortcuts import render
from .models import Coin

# Create your views here.
def get_coins():
    
    coins = Coin.objects.all()
    return coins
def get_featured_coins():
    featured_coins = Coin.objects.all()[:3]
    return featured_coins