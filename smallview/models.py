from django.db import models

class Album(models.Model):  #models.Model allows model store data to database
    image = models.ImageField(upload_to='images/')  #see jango doc for more model field reference and parameters
    summary = models.CharField(max_length=200)
