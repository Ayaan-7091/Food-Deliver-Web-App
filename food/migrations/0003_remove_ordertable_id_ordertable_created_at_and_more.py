# Generated by Django 4.2.3 on 2023-12-10 08:35

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_ordertable_alter_food_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordertable',
            name='id',
        ),
        migrations.AddField(
            model_name='ordertable',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='ordertable',
            name='order_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='food',
            name='food_id',
            field=models.AutoField(default=datetime.datetime(2023, 12, 10, 8, 35, 23, 481799, tzinfo=datetime.timezone.utc), primary_key=True, serialize=False),
        ),
    ]
