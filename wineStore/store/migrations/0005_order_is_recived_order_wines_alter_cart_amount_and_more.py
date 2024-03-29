# Generated by Django 5.0 on 2023-12-20 08:39

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order_account_id_alter_client_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_recived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='wines',
            field=models.ManyToManyField(to='store.wine'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='amount',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(limit_value=1)]),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_of_birth',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2005, 12, 24))]),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_set_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 20, 9, 39, 26, 139976)),
        ),
    ]
