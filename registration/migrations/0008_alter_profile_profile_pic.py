# Generated by Django 3.2.4 on 2021-06-18 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
    ]
