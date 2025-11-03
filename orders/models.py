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
        return selfrom django.db import models
from .models import OrderStatus  # make sure this import exists or adjust if both models are in same file

class Order(models.Model):
    order_number = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # 👇 Add this line
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)

    def _str_(self):
        return self.order_number
4:50 PM
f.name
from django.db import models

class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def _str_(self):
        return self.name