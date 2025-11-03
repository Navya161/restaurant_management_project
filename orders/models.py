from django.db import models

# Create your models here.
from django.db import models

class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    PENDING = 'Pending'
    PROCESSING = 'Processing'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'

    def _str_(self):
        return self.name