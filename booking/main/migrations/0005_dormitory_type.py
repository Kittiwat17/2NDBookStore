# Generated by Django 3.0.5 on 2020-04-26 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_dormitory_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='dormitory',
            name='type',
            field=models.CharField(choices=[('female', 'female'), ('male', 'male')], default='found', max_length=255),
        ),
    ]
