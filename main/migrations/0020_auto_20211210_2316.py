# Generated by Django 3.2.9 on 2021-12-10 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20211210_0251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user_id',
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]