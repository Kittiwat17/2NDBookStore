# Generated by Django 3.2.3 on 2021-05-16 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_alter_typebook_select'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typebook',
            name='select',
            field=models.CharField(choices=[('sell', 'sell'), ('buy', 'buy')], default='', max_length=50),
        ),
    ]
