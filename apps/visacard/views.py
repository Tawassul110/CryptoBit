from django.shortcuts import render
from .models import Visacard

# Create your views here.
def get_visacard ():

    visacard = Visacard.objects.all()
    return visacard
