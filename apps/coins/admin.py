from django.contrib import admin
from .models import Coin
from .models import Customer

# Register your models here.
admin.site.register(Coin)
admin.site.register(Customer)
