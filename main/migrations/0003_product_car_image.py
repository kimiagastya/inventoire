# Generated by Django 4.2.5 on 2023-10-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='car_image',
            field=models.ImageField(default=1, upload_to='product_images/'),
            preserve_default=False,
        ),
    ]