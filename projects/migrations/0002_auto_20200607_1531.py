# Generated by Django 3.0.6 on 2020-06-07 15:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 7, 7, 15, 31, 15, 940278)),
        ),
    ]
