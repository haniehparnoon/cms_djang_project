# Generated by Django 3.2.9 on 2022-02-04 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsApp', '0003_alter_credit_customer_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='cart_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(17)]),
        ),
    ]
