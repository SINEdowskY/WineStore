# Generated by Django 5.0 on 2023-12-13 14:46

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address_apartament_number',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_of_birth',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2005, 12, 17))]),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='zip_code',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='give valid postal code in format: XX-XXX', regex='^\\d{2}-\\d{3}$')]),
        ),
    ]
