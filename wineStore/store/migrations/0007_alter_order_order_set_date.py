# Generated by Django 5.0 on 2023-12-20 09:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_order_order_set_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_set_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 20, 10, 31, 42, 487844)),
        ),
    ]
