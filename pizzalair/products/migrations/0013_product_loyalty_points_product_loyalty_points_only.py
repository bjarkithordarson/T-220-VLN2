# Generated by Django 4.2 on 2023-05-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_merge_20230512_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='loyalty_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='loyalty_points_only',
            field=models.BooleanField(default=False),
        ),
    ]
