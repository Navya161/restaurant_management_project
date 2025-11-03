from django.db import models
class MenuCategory(models.Models):
    name=models.CharField(max_length=100)
    
# Create your models here.
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)  # 👈 NEW FIELD

    def __str__(self):
        return self.name
