from django.db import models

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=90)
    logo_image = models.ImageField(upload_to="uploads/coins")
    price = models.FloatField()
    details = models.TextField()

    def __str__(self):
        return self.name 

