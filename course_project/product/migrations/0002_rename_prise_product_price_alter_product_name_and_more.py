# Generated by Django 4.0.6 on 2022-07-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prise',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor_code',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
