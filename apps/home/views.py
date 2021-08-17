from django.shortcuts import render
from apps.coins.views import get_coins

# Create your views here.
def home(request):
    context = {
        'coins' : get_coins()
    }
    return render(request, 'pages/index.html', context)

def trade(request):
    return render(request, 'pages/express.html')


def market(request):
    return render(request, 'pages/market.html')


def visacard(request):
    return render(request, 'pages/visacard.html')


def forgotpassword(request):
    return render(request, 'pages/forgotpassword.html')


def register(request):
    return render(request, 'pages/register.html')


def login(request):
    return render(request, 'pages/login.html')

def details(request):
    return render(request, 'pages/details.html')    