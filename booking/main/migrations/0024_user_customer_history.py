# Generated by Django 3.0.5 on 2020-04-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20200428_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_customer',
            name='history',
            field=models.IntegerField(null=True),
        ),
    ]