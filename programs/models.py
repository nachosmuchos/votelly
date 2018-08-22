from django.db import models

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='Desctiption')
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name[:100]
