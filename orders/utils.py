from datetime import date
from django.db.models import Sum
from .models import Order  # Assumes Order model is in the same app

def get_daily_sales_total(target_date):
    """
    Returns the total sales for a given date by summing total_price of all orders created on that date.
    If no orders are found, returns 0.
    """
    result = (
        Order.objects.filter(created_at__date=target_date)
        .aggregate(total_sum=Sum('total_price'))
    )
    total = result['total_sum'] or 0
    return total