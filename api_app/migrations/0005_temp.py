# Generated by Django 4.2.4 on 2023-09-26 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0004_posts_rates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
