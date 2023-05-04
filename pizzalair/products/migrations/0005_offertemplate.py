# Generated by Django 4.2 on 2023-05-04 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_productcategory_product_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Offer', to='products.offer')),
            ],
        ),
    ]
