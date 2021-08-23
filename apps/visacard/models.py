from django.db import models

# Create your models here.
class Visacard(models.Model):
    title = models.CharField(max_length=300, null=True)
    content = models.TextField(max_length=600, null=True)
    featured_image = models.ImageField(upload_to="media/visacard")
    
    def __str__(self):
        return self.title

