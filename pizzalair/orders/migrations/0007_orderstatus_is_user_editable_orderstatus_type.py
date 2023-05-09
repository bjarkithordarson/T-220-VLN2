# Generated by Django 4.2 on 2023-05-08 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_orderpaymentmethod_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderstatus',
            name='is_user_editable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderstatus',
            name='type',
            field=models.CharField(choices=[(1, 'Initial'), (2, 'Received'), (3, 'Processing'), (4, 'Finished'), (5, 'Cancelled')], default=1, max_length=255),
        ),
    ]
