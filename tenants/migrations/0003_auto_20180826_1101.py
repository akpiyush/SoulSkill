# Generated by Django 2.1 on 2018-08-26 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0002_auto_20180826_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
