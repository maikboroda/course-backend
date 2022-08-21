# Generated by Django 4.0.6 on 2022-07-31 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('vendor_code', models.CharField(max_length=255)),
                ('prise', models.FloatField()),
            ],
        ),
    ]