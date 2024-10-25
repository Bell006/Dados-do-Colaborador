from django.db import models
import datetime

class Colab(models.Model):
    email = models.CharField(max_length=64)
    name = models.EmailField(max_length=64)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.name} - {self.email}'

