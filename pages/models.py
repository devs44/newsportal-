from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Trending(models.Model):
    picture = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=250)
    description = RichTextField()

    def __str__(self):
        return self.title
