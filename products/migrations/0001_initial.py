# Generated by Django 4.0.5 on 2022-09-08 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('deliveryTime', models.DateTimeField()),
                ('mkuStudent', models.BooleanField()),
                ('deliveryPoint', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('deliveryTime',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField(default='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='products/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('get_image_str', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Products_galore',
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='profile/')),
                ('get_image_str', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SelectedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField(default='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='products/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('get_image_str', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'SelecProducts_galore',
                'ordering': ('name',),
                'abstract': False,
            },
        ),
    ]
