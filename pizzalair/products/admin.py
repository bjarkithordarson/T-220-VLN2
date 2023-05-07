from django.contrib import admin

# Register your models here.

from .models import Product
from .models import Pizza
from .models import ProductCategory
from .models import Offer


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']

admin.site.register(Product, ProductAdmin, )

class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Pizza)
admin.site.register(ProductCategory)
admin.site.register(Offer)
