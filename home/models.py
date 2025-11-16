from django.db import models

class DailySpecial(models.Model):
    # assuming your existing fields, e.g.:
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    @staticmethod
    def get_random_special():
        """
        Returns a single random DailySpecial instance.
        If no specials are available, returns None.
        """
        random_special = DailySpecial.objects.order_by('?').first()
        return random_special
Explanation