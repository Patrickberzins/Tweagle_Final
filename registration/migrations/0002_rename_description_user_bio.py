# Generated by Django 3.2.4 on 2021-06-08 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='description',
            new_name='bio',
        ),
    ]
