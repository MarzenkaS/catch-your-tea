# Generated by Django 3.2.25 on 2024-07-05 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='full_name',
            new_name='default_full_name',
        ),
    ]