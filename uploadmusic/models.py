from django.db import models

# Create your models here.

class Uploadmusic(models.Model):
    image = models.ImageField(upload_to='images/')
    music = models.FileField(upload_to='music/')
    title = models.CharField(max_length=100 , blank=True , null=True)
    description = models.TextField(max_length=100 , blank=True , null=True)

    def __str__(self):
        return self.title