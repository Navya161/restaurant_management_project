from django.shortcuts import render

# Create your views here.
from.utils import generate_unique_coupon_code
from.models import Coupon
def Create_coupon():
    code =generate_unique_coupon_code(Coupon,field="code",length=12)
    coupon = Coupon.objects.create(code=code,discount=10)
    return coupon
    
