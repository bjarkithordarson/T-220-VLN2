# Generated by Django 4.2 on 2023-05-04 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_offertemplate'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='Category', to='products.productcategory')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.offer')),
            ],
        ),
        migrations.DeleteModel(
            name='OfferTemplate',
        ),
    ]
