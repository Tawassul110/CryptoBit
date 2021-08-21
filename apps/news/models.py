from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=90)
    content = models.TextField()
    publish_date = models.DateField()
    featured_image = models.ImageField (upload_to="media/news", height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = ("News")
        verbose_name_plural = ("News")

    def __str__(self):
        return self.title

    
