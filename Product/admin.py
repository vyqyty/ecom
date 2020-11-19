from django.contrib import admin

# Register your models here.
from Product.models import Category, Product


admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'updated_at']
    list_filter = ['title', 'created_at']
    list_per_page = 10
    search_fields = ['title', 'new_price', 'detail']


admin.site.register(Product, ProductAdmin)
