# Generated by Django 3.0.3 on 2020-03-04 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionProductos', '0003_auto_20200304_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='photos_category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='photos_products'),
        ),
    ]
