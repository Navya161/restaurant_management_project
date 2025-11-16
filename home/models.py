port datetime
from django.db import models

class DailySpecialManager(models.Manager):
    def upcoming(self):
        """
        Returns DailySpecial objects where the date is today or in the future.
        """
        today = datetime.date.today()
        return super().get_queryset().filter(date__gte=today)


class DailySpecial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()

    # Attach the custom manager
    objects = DailySpecialManager()

    def __str__(self):
        return f"{self.name} - {self.date}"
