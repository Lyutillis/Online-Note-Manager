# Generated by Django 4.1 on 2023-02-03 13:55

import User.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='profile_pics/default_pic.gif', null=True, upload_to=User.models.image_upload_handler),
        ),
    ]
