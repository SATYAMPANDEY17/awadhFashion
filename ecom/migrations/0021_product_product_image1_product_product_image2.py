# Generated by Django 4.2.4 on 2024-05-18 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0020_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image1',
            field=models.ImageField(blank=True, null=True, upload_to='product_image/'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image2',
            field=models.ImageField(blank=True, null=True, upload_to='product_image/'),
        ),
    ]
