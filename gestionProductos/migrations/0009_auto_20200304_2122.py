# Generated by Django 3.0.3 on 2020-03-05 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionProductos', '0008_auto_20200304_1013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-parentCategory']},
        ),
    ]
