# Generated by Django 3.0.6 on 2020-06-07 15:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200607_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 7, 7, 15, 49, 41, 875466)),
        ),
    ]
