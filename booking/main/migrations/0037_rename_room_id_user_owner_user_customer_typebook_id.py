# Generated by Django 3.2.3 on 2021-05-15 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20210515_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_owner_user_customer',
            old_name='room_id',
            new_name='typebook_id',
        ),
    ]