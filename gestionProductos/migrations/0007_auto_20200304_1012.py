# Generated by Django 3.0.3 on 2020-03-04 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionProductos', '0006_auto_20200304_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='photos_category'),
        ),
    ]
