# Generated by Django 3.2.9 on 2021-11-26 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_rooms_room_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='room_image',
            field=models.ImageField(upload_to='photos/%Y/%m/%d'),
        ),
    ]
