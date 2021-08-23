from django.db import models

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=90)
    logo_image = models.ImageField(upload_to="media/coins")
    price = models.FloatField()
    details = models.TextField()
    working = models.TextField(null=True)
    advantages = models.TextField(null=True)
    disadvantages = models.TextField(null=True)
    coin_short_name = models.CharField(null=True, max_length=300)
    sparkline = models.ImageField(upload_to="media/coins" , null=True)

    def __str__(self):
        return self.name 

