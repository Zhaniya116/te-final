# Generated by Django 4.2.6 on 2024-02-08 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accommodation',
            old_name='city',
            new_name='destination_city',
        ),
    ]
