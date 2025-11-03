
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    has_delivery = models.BooleanField(default=False)  # ✅ new field

    def __str__(self):
        return self.name