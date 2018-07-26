from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=200)
    number_of_votes = models.IntegerField(default=0)
