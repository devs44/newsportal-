from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Latest(models.Model):
    banner_img = models.ImageField(upload_to='images/')
    banner_title = models.CharField(max_length=250)
    description = RichTextField()
    small_desc = RichTextField()
    small_img = models.ImageField(upload_to='images/')
    



    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
