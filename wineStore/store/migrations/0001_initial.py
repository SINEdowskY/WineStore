# Generated by Django 5.0 on 2023-12-13 13:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('type', models.CharField(choices=[('red', 'Red'), ('white', 'White'), ('rose', 'Rose'), ('sparkling', 'Sparkling')], max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('grape_type', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=400)),
                ('pairs_well', models.CharField(choices=[('Chicken and Turkey', 'Chicken Turkey'), ('Duck and Goose', 'Duck Goose'), ('Pork', 'Pork'), ('Lamb', 'Lamb'), ('Beef and Venison', 'Beef N Venison'), ('Green Vegetables', 'Green Veg'), ('Root Vegetables', 'Root Veg'), ('Mushroom', 'Mushroom'), ('Tomato-based', 'Tomato'), ('Spicy', 'Spicy'), ('White Fish', 'White Fish'), ('Meaty and Oily Fish', 'Meaty Oily Fish'), ('Shellfish, Crab and Lobster', 'Shellfish'), ("Goats' Cheese and Feta", 'Gcheese Feta'), ('Manchego and Parmesan', 'Manchego Parmesan'), ('Cheddar and Gruyere', 'Cheddar Gruyere'), ('Blue Cheese', 'Blue Cheese'), ('Brie and Camembert', 'Brie Camembert'), ('Fruit-based Desserts', 'Fruit Based'), ('Chocolate and Caramel', 'Choco Caramel'), ('Cakes and Cream', 'Cake Cream')], max_length=30)),
                ('origin_country', models.CharField(default='France', max_length=20)),
                ('storage_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('address_street', models.CharField(max_length=50)),
                ('address_number', models.CharField(max_length=3)),
                ('address_apartament_number', models.CharField(max_length=3)),
                ('zip_code', models.CharField(max_length=6)),
                ('phone_number', models.CharField(max_length=9)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_value', models.DecimalField(decimal_places=2, max_digits=12)),
                ('order_set_date', models.DateField()),
                ('shipment', models.CharField(choices=[('InPost', 'Inpost'), ('Poczta Polska', 'Post'), ('DHL', 'Dhl')], default='InPost', max_length=20)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.client')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.wine')),
            ],
        ),
    ]
