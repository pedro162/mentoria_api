from django.db import models
from django.core.validators import MinValueValidator, URLValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category Name")
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name="Category Description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Product Name")
    description = models.CharField(max_length=1000, blank=True, null=True, verbose_name="Product Description")
    price = models.DecimalField(max_digits=60, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="Price")
    stock_quantity = models.PositiveIntegerField(validators=[MinValueValidator(0)], verbose_name="Stock Quantity")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Category")
    image = models.URLField(max_length=500, blank=True, null=True, validators=[URLValidator()], verbose_name="Image URL")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
