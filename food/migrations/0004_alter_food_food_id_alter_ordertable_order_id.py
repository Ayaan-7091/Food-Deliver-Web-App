# Generated by Django 4.2.3 on 2023-12-10 08:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_remove_ordertable_id_ordertable_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food_id',
            field=models.AutoField(default=datetime.datetime(2023, 12, 10, 8, 48, 31, 18672, tzinfo=datetime.timezone.utc), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ordertable',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
