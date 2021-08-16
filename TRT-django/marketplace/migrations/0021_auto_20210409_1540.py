# Generated by Django 3.1.7 on 2021-04-09 19:40

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0020_auto_20210408_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='deadline',
            field=models.DateField(help_text='Latest allowed is 2022-04-09', validators=[django.core.validators.MinValueValidator(datetime.date(2021, 4, 9)), django.core.validators.MaxValueValidator(datetime.date(2022, 4, 9))]),
        ),
        migrations.AlterField(
            model_name='itemrequest',
            name='deadline',
            field=models.DateField(help_text='Latest allowed is 2022-04-09', validators=[django.core.validators.MinValueValidator(datetime.date(2021, 4, 9)), django.core.validators.MaxValueValidator(datetime.date(2022, 4, 9))]),
        ),
    ]
