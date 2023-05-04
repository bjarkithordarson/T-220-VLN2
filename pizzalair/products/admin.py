from django.contrib import admin

# Register your models here.

from .models import Product, ProductCategory, Pizza, Offer, OfferComponent


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']

admin.site.register(Product, ProductAdmin, )

admin.site.register(Pizza)
admin.site.register(ProductCategory)
admin.site.register(Offer)
admin.site.register(OfferComponent)
