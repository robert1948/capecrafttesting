# Generated by Django 4.2.5 on 2024-01-14 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='address',
            name='zipcode',
            field=models.IntegerField(),
        ),
    ]
