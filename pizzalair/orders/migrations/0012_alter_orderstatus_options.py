# Generated by Django 4.2 on 2023-05-09 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_orderstatus_order_status_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderstatus',
            options={'verbose_name_plural': 'Order statuses'},
        ),
    ]
