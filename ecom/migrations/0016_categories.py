# Generated by Django 4.2.8 on 2024-05-11 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0015_alter_customer_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
