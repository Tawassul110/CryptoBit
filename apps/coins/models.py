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

class Customer(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    acc_no = models.IntegerField(max_length=14)
    quantity = models.SmallIntegerField()

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Customer_detail", kwargs={"pk": self.pk})