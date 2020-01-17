# Generated by Django 3.0 on 2019-12-09 19:13

import backend.product.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('description', models.TextField(max_length=50)),
                ('photo', models.ImageField(upload_to=backend.product.models.room_directory_path)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='auth_app.Business')),
            ],
        ),
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_lists', to='auth_app.Business')),
                ('products', models.ManyToManyField(related_name='product_lists', to='product.Product')),
            ],
        ),
    ]
