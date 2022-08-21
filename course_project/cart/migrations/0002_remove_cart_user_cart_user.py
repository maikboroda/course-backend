# Generated by Django 4.0.6 on 2022-08-08 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_tel'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ManyToManyField(to='user.user'),
        ),
    ]