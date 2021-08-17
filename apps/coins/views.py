from django.shortcuts import render
from .models import Coin

# Create your views here.
def get_coins():
    
    coins = Coin.objects.all()
    return coins
