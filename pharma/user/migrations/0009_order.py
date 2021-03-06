# Generated by Django 3.0 on 2020-06-06 15:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20200601_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('date_of_order', models.DateField(default=django.utils.timezone.now)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Medicine')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.patientsPersonalDetail')),
            ],
        ),
    ]
