from django.urls import path, include
from .views import hello
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register('api/categories', CategoryViewSet)
router.register('api/products', ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('hello/', hello,  name="hello"),
]
