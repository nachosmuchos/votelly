from django.db import models
from characters.models import Character

# Create your models here.
class Comment(models.Model):
    comment = models.CharField(max_length=250)
    comment_time = models.DateTimeField()
    related_program = models.ForeignKey(Character, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.comment
