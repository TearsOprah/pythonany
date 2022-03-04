from dataclasses import field
from pyexpat import model
from re import search
from django.contrib import admin
from products.models import Product, ProductCategory, Basket
from users.views import register


admin.site.register(ProductCategory)
# admin.site.register(Product)
admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name',)


class BasketAdminInline(admin.TabularInline):
    model = Basket
    field = ('product', 'quantity', 'created_timestamp')
    extra = 0