from django.urls import path
from .views import MenuItemSearchViewSet

menu_search_list = MenuItemSearchViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('menu-items/search/', menu_search_list, name='menuitem-search'),
]