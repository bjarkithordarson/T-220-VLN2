from django.db import models
from django.utils.html import mark_safe
from django.utils.text import slugify


class ProductCategory(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, null=True)
    filter = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField(default=0)
    pay_with_loyalty_points = models.BooleanField(default=False)
    loyalty_points_bonus = models.IntegerField(default=0)
    description = models.TextField()
    category = models.ManyToManyField(ProductCategory, related_name='products')
    picture = models.ImageField()
    def img_preview(self): #new
        return mark_safe('<img src = "{url}" width = "300"/>'.format(
             url=self.picture.url
         ))

    def type(self):
        return self.__class__.__name__.lower()

    def __str__(self):
        return self.name


class Pizza(Product):
    #product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='Pizza')
    toppings = models.CharField(max_length=120)

class Offer(Product):
    pass
    #product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='Offer')
    #template = models.CharField(max_length=120)

class OfferTemplate(models.Model):
    offer = models.ForeignKey(Offer, blank=True, null=True, on_delete=models.CASCADE, related_name="templates")
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, on_delete=models.CASCADE)

    def quantity_as_range(self):
        return range(self.quantity)

    def products(self):
        return Product.objects.filter(category=self.category)

class OfferInstance(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='type')
    products = models.ManyToManyField(Product, related_name='products')

    def __str__(self):
        return f"{self.offer.name} - {', '.join([str(product) for product in self.products.all()])}"
