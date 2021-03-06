# Generated by Django 3.2.3 on 2021-05-14 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20200430_0150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameB', models.CharField(default='', max_length=255)),
                ('Author', models.CharField(default='', max_length=255)),
                ('Year', models.CharField(default='', max_length=255)),
                ('Language', models.CharField(default='', max_length=255)),
                ('Contact', models.TextField(max_length=255)),
                ('Detail', models.CharField(default='', max_length=255)),
                ('Picture', models.ImageField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Typebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_book_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.book')),
            ],
        ),
        migrations.RemoveField(
            model_name='dormitory',
            name='user_Owner_user_id',
        ),
        migrations.RemoveField(
            model_name='furniture',
            name='romm_room_id',
        ),
        migrations.RemoveField(
            model_name='picture_room',
            name='room_room_id',
        ),
        migrations.RemoveField(
            model_name='room',
            name='dormitory_dormitory_id',
        ),
        migrations.RemoveField(
            model_name='user_customer',
            name='history',
        ),
        migrations.RemoveField(
            model_name='user_customer',
            name='romm_room_id',
        ),
        migrations.RemoveField(
            model_name='user_customer',
            name='user_user_id',
        ),
        migrations.RemoveField(
            model_name='user_owner_user_customer',
            name='create_by',
        ),
        migrations.RemoveField(
            model_name='user_owner_user_customer',
            name='room_id',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Dormitory',
        ),
        migrations.DeleteModel(
            name='Furniture',
        ),
        migrations.DeleteModel(
            name='picture_room',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='user_customer',
        ),
        migrations.DeleteModel(
            name='user_owner_user_customer',
        ),
    ]
