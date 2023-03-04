from django.db import models

# Create your models here.
class Place(models.Model):
    Name=models.CharField(max_length=250)
    Image=models.ImageField(upload_to='pics')
    Description=models.TextField()


class Team(models.Model):
    Name = models.CharField(max_length=250)
    Image = models.ImageField(upload_to='pics')
    Description = models.TextField()









