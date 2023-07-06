from django.db import models

class Simple_Project(models.Model):
    # Create your models here.
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
