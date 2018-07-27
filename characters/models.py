from django.db import models
from programs.models import Program

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=200)
    number_of_votes = models.IntegerField(default=0)
    related_program = models.ForeignKey(Program, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name[:100]
