# Generated by Django 3.0.5 on 2020-04-28 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0022_user_owner_user_user_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_owner_user_customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=50, null=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Room')),
            ],
        ),
        migrations.DeleteModel(
            name='user_owner_user_user_customer',
        ),
    ]