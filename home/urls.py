from django.urls import path
from .views import *

urlpatterns = [
    
]from django.urls import path
from .views import FeaturedMenuItemsView

urlpatterns = [
    path('menu/featured/', FeaturedMenuItemsView.as_view(), name='featured-menu-items'),
]