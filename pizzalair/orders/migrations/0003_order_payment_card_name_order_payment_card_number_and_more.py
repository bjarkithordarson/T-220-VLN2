# Generated by Django 4.2 on 2023-05-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_card_name',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_card_number',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_cvc',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_expiry_month',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_expiry_year',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='billing_address',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='billing_city',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='billing_country',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='billing_name',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='billing_postal_code',
            field=models.CharField(null=True),
        ),
    ]