# Generated by Django 4.2.4 on 2023-10-05 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
