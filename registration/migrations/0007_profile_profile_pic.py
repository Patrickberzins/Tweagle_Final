# Generated by Django 3.2.4 on 2021-06-18 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_delete_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]