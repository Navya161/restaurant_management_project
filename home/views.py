from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer

class MenuCategoryListAPIView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer  # make sure this exists

class FeaturedMenuItemsView(generics.ListAPIView):
    queryset = MenuItem.objects.filter(is_featured=True)
    serializer_class = MenuItemSerializer
= MenuCategorySerializer