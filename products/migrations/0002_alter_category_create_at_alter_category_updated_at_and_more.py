# Generated by Django 4.2 on 2024-07-18 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='create_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='create_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='updated_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
