# Generated by Django 3.0.5 on 2020-04-29 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20200429_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='Send_request',
            field=models.BooleanField(null=True),
        ),
    ]
