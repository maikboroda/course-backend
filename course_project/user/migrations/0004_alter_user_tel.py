# Generated by Django 4.0.6 on 2022-08-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tel',
            field=models.BigIntegerField(unique=True),
        ),
    ]
