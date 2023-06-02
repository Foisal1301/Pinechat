# Generated by Django 4.0.6 on 2022-08-01 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friend', '0003_rename_reciever_messagewithfriend_receiver_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendrequest',
            old_name='reciever',
            new_name='receiver',
        ),
        migrations.AlterField(
            model_name='messagewithfriend',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
    ]
