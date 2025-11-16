rom decimal import Decimal, ROUND_HALF_UP

def calculate_tip_amount(order_total, tip_percentage):
    """
    Calculates the tip amount for a given order total and tip percentage.

    Args:
        order_total (Decimal or float): The total bill before tip.
        tip_percentage (int): The tip percentage (e.g., 15 for 15%).

    Returns:
        Decimal: Tip amount, rounded to two decimal places.
    """
    # Ensure order_total is Decimal for precision
    total = Decimal(str(order_total))
    tip = (total * Decimal(tip_percentage) / Decimal('100')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return tip
This 