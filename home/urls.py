from django.urls import path
from .views import *

urlpatterns = [
    
]from django.urls import path
from .views import FeaturedMenuItemsView

urlpatterns = [
    path('menu/featured/', FeaturedMenuItemsView.as_view(), name='featured-menu-items'),
]from django.urls import path
from .views import OrderHistoryView

urlpatterns = [
    path('orders/history/', OrderHistoryView.as_view(), name='order-history'),
]
