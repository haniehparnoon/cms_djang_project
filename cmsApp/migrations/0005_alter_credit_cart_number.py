# Generated by Django 3.2.9 on 2022-02-04 12:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsApp', '0004_alter_credit_cart_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='cart_number',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(16)]),
        ),
    ]
