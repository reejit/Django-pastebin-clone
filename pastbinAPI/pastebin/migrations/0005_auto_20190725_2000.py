# Generated by Django 2.2.3 on 2019-07-25 17:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0004_auto_20190725_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
