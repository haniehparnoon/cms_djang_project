# Generated by Django 3.2.9 on 2022-02-03 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ordered', 'ordered'), ('paid', 'paid')], default='ordered', max_length=7),
        ),
    ]
