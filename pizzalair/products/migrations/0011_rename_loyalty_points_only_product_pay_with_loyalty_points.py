# Generated by Django 4.2 on 2023-05-11 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_rename_loyalty_points_product_loyalty_points_bonus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='loyalty_points_only',
            new_name='pay_with_loyalty_points',
        ),
    ]