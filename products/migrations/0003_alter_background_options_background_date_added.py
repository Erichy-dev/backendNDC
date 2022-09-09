# Generated by Django 4.0.5 on 2022-09-08 09:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_background'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='background',
            options={'ordering': ('date_added',)},
        ),
        migrations.AddField(
            model_name='background',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]