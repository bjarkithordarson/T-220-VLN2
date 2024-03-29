# Generated by Django 4.2 on 2023-05-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_orderstatus_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatus',
            name='type',
            field=models.IntegerField(choices=[(1, 'Initial'), (2, 'Received'), (3, 'Processing'), (4, 'Finished'), (5, 'Cancelled')], default=1),
        ),
    ]
