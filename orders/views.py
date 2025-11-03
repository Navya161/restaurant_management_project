from django.shortcuts import render

# Create your views here.
from.utils import generate_unique_coupon_code
from.models import Coupon
def Create_coupon():
    code =generate_unique_coupon_code(Coupon,field="code",length=12)
    coupon = Coupon.objects.create(code=code,discount=10)
    return coupon
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Coupon

class CouponValidationView(APIView):
    def post(self, request):
        code = request.data.get('code')

        if not code:
            return Response(
                {"error": "Coupon code is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            coupon = Coupon.objects.get(code__iexact=code)
        except Coupon.DoesNotExist:
            return Response(
                {"error": "Invalid coupon code."},
                status=status.HTTP_400_BAD_REQUEST
            )

        today = timezone.now().date()
        if not coupon.is_active:
            return Response({"error": "This coupon is not active."}, status=status.HTTP_400_BAD_REQUEST)
        if coupon.valid_from > today or coupon.valid_until < today:
            return Response({"error": "This coupon has expired or is not yet valid."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {
                "message": "Coupon is valid.",
                "code": coupon.code,
                "discount_percentage": coupon.discount_percentage,
            },
            status=status.HTTP_200_OK
        )
