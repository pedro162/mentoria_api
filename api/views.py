from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, generics, filters
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

@api_view(["GET"])
def hello(request):
    """
    Um endpoint simples para teste.
    ---
    responses:
      200:
        description: Retorno simples
    """
    
    return Response({"message": "Hello from Django REST API!"})

class CategoryViewSet(viewsets.ModelViewSet):
    """
    View description
    - Endpoint for resources management

    Allowed methods:
    - GET: Returns a resource list
    - POST: Creates a new resource
    - PUT: Updates a existing resource
    - DELETE: Removes a existing resource
    """
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['name', 'description', 'created_at', 'updated_at']
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class ProductViewSet(viewsets.ModelViewSet):
    """
        View description
        - Endpoint for resources management

        Allowed methods:
        - GET: Returns a resource list
        - POST: Creates a new resource
        - PUT: Updates a existing resource
        - DELETE: Removes a existing resource
        """
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['name', 'description','price', 'stock_quantity', 'created_at', 'updated_at']
    filterset_class = ProductFilter
    permission_classes = [IsAuthenticatedOrReadOnly]