# Generated by Django 3.0.5 on 2020-04-29 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20200429_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='Send_request',
            field=models.BooleanField(default=False),
        ),
    ]