# Generated by Django 3.0 on 2020-05-30 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200530_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientspersonaldetail',
            name='status',
        ),
    ]