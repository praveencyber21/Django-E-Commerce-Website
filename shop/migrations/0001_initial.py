# Generated by Django 5.0.6 on 2024-05-27 07:03

import django.db.models.deletion
import shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=shop.models.getFileName)),
                ('description', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-hidden, 1-show')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('vendor', models.CharField(max_length=150)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=shop.models.getFileName)),
                ('quantity', models.IntegerField()),
                ('original_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('description', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-hidden, 1-show')),
                ('trending', models.BooleanField(default=False, help_text='0-default, 1-trending')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
    ]
