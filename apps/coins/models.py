from django.db import models

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=90)
    logo_image = models.ImageField(upload_to="media/coins")
    price = models.FloatField()
    details = models.TextField()
    working = models.TextField(max_length=300, null=True)
    advantages = models.TextField(max_length=300, null=True)
    disadvantages = models.TextField(max_length=300, null=True)

    def __str__(self):
        return self.name 

