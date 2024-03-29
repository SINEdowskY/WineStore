# Generated by Django 5.0 on 2024-01-16 16:12

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_wineorder_amount_alter_client_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='alcohol_percentage',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='wine',
            name='wine_year',
            field=models.IntegerField(default=2001),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_of_birth',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2006, 1, 20))]),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_set_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 16, 17, 12, 8, 421113)),
        ),
    ]
