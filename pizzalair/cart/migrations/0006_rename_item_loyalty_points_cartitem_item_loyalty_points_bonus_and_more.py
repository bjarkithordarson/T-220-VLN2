# Generated by Django 4.2 on 2023-05-11 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_cartitem_item_loyalty_points'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='item_loyalty_points',
            new_name='item_loyalty_points_bonus',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='pay_with_loyalty_points',
            field=models.BooleanField(default=False),
        ),
    ]