# Generated by Django 3.0.1 on 2020-05-29 15:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='patientsPersonalDetails',
            new_name='patientsPersonalDetail',
        ),
    ]
