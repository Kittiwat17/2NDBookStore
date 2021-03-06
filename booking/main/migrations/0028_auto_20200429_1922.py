# Generated by Django 3.0.5 on 2020-04-29 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20200429_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='Room_picture1',
        ),
        migrations.RemoveField(
            model_name='room',
            name='Room_picture2',
        ),
        migrations.RemoveField(
            model_name='room',
            name='Room_picture3',
        ),
        migrations.RemoveField(
            model_name='room',
            name='Room_picture4',
        ),
        migrations.RemoveField(
            model_name='room',
            name='Room_picture5',
        ),
        migrations.CreateModel(
            name='picture_room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_picture1', models.ImageField(default='', null=True, upload_to='')),
                ('Room_picture2', models.ImageField(default='', null=True, upload_to='')),
                ('Room_picture3', models.ImageField(default='', null=True, upload_to='')),
                ('Room_picture4', models.ImageField(default='', null=True, upload_to='')),
                ('Room_picture5', models.ImageField(default='', null=True, upload_to='')),
                ('room_room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Room')),
            ],
        ),
    ]
