from django.db import models

class Mainpage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50) 
    image = models.FilePathField(path="/img")
