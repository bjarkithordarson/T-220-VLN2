# Generated by Django 4.2 on 2023-05-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_orderpaymentmethod_remove_order_is_paid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderpaymentmethod',
            name='method',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
