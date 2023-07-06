from django.db import models

class Simple_Project(models.Model):
    # Create your models here.
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
