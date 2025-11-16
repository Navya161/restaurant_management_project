from datetime import datetime, time

def is_restaurant_open():
    """
    Returns True if the restaurant is currently open, False otherwise.
    Example hours:
    - Monday–Friday: 9 AM to 10 PM
    - Saturday–Sunday: 10 AM to 11 PM
    """

    now = datetime.now()
    current_day = now.weekday()      # Monday=0, Sunday=6
    current_time = now.time()

    # Define opening hours
    weekday_open = time(9, 0)        # 9:00 AM
    weekday_close = time(22, 0)      # 10:00 PM

    weekend_open = time(10, 0)       # 10:00 AM
    weekend_close = time(23, 0)      # 11:00 PM

    # Check weekday hours (Mon–Fri)
    if current_day <= 4:
        return weekday_open <= current_time <= weekday_close
    
    # Check weekend hours (Sat–Sun)
    else:
        return weekend_open <= current_time <= weekend_close