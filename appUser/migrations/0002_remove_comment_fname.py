# Generated by Django 4.2.2 on 2023-08-11 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='fname',
        ),
    ]
