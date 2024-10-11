from django.db import models
from django.utils import timezone

# Create your models here.
class CoffeeSeq(models.Model):
    COFFEE_TYPE_CHOICE = [
        ("CC", "COLD COFFEE"),
        ("HC", "HOT COFFEE"),
        ("MC", "MILK COFFEE"),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=COFFEE_TYPE_CHOICE)


def __str__(self):
    return self.name
