from django.utils import timezone
from .models import DailyOperatingHours  # adjust to the actual app if needed

def get_today_operating_hours():
    """
    Return (open_time, close_time) for today's operating hours.
    If no DesktopOperatingHours entry exists for today, return (None, None).
    Uses Django's timezone to respect project settings.
    """
    # Get today's weekday name, e.g., 'Monday'
    today_name = timezone.localtime().strftime('%A')

    try:
        hours = DailyOperatingHours.objects.get(day=today_name)
        return (hours.open_time, hours.close_time)
    except DailyOperatingHours.DoesNotExist:
        return (None, None)
Notes: