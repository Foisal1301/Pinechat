# Generated by Django 4.0.6 on 2022-08-02 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profile_bio_profile_profile_pic_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='otp',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
