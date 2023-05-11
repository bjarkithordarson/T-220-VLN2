from django.contrib import admin

# Register your models here.

from .models import Product, OfferInstance
from .models import Pizza
from .models import ProductCategory
from .models import Offer
from .models import OfferTemplate


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ('id', 'name', 'price', 'img_preview')

admin.site.register(Product, ProductAdmin, )

class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', 'slug', 'filter')

class PizzaAdmin(ProductAdmin):
    pass

class OfferAdmin(ProductAdmin):
    pass

class OfferTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'offer', 'quantity', 'category')

admin.site.register(Pizza, PizzaAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(OfferTemplate, OfferTemplateAdmin)
admin.site.register(OfferInstance)
