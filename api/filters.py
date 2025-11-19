import django_filters
from .models import Product,Category

class ProductFilter(django_filters.FilterSet):

    # Text filters (contains / icontains)
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains", label="Name contains")
    description = django_filters.CharFilter(field_name="description", lookup_expr="icontains", label="Description contains")

    # Numeric filters (exact and ranges)
    price = django_filters.NumberFilter(field_name="price", label="Exact price")
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte", label="Minimum price")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte", label="Maximum price")

    stock_quantity = django_filters.NumberFilter(field_name="stock_quantity",  label="Exact stock")
    min_stock_quantity = django_filters.NumberFilter(field_name="stock_quantity", lookup_expr="gte", label="Min stock")
    max_stock_quantity = django_filters.NumberFilter(field_name="stock_quantity", lookup_expr="lte", label="Max stock")

    # Foreign key filter
    category = django_filters.ModelChoiceFilter(field_name="category", queryset=Category.objects.all(), label="Category")

    # Date filters
    before_created_at = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="lte", label="Created before")
    after_created_at = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="gte", label="Created after")

    before_updated_at = django_filters.DateTimeFilter(field_name="updated_at", lookup_expr="lte", label="Updated before")
    after_updated_at = django_filters.DateTimeFilter(field_name="updated_at", lookup_expr="gte", label="Updated after")

    class Meta:
        model = Product
        fields = []
