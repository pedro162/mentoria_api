from django.contrib import admin
from .models import Product, Category
# Register your models here.
# docker compose exec web bash

@admin.register(Product)
class Products(admin.ModelAdmin):
    list_display = ("id", "name", "category", "description", "stock_quantity", "price", "created_at", "updated_at")
    search_fields = ("name", "description","category__name")
    list_filter = ("created_at",)
    ordering = ("id", "name", "description")
    list_editable = ("price", "stock_quantity", "category")

    

@admin.register(Category)
class Categories(admin.ModelAdmin):
    list_display = ("id", "name", "description", "created_at", "updated_at")
    search_fields = ("name", "description",)
    list_filter = ("created_at",)
    