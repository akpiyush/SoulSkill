# Generated by Django 2.1 on 2018-08-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0005_auto_20180826_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Contact',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
