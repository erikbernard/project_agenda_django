from django.db import models
from django.utils import  timezone


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    emai = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    descrition = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
