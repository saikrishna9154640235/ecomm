# Generated by Django 4.2 on 2024-07-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_qunatity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qunatity',
            field=models.IntegerField(default=1),
        ),
    ]
