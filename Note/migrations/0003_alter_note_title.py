# Generated by Django 4.1 on 2023-02-07 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Note', '0002_note_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(default='No Title', max_length=1000),
        ),
    ]