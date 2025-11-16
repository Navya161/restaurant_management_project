rom rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemPagination(PageNumberPagination):
    page_size = 10  # Adjust as needed

class MenuItemSearchViewSet(viewsets.ViewSet):
    """
    API endpoint that allows searching menu items by name.
    """
    pagination_class = MenuItemPagination

    def list(self, request):
        query = request.GET.get('q', '')
        queryset = MenuItem.objects.all()
        if query:
            queryset = queryset.filter(name__icontains=query)
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        serializer = MenuItemSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
