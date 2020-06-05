# Generated by Django 3.0 on 2020-06-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_patientspersonaldetail_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.CharField(max_length=50)),
                ('med_brand', models.CharField(max_length=100)),
                ('med_stock', models.IntegerField(default=0)),
                ('med_price', models.IntegerField(default=0)),
                ('med_type', models.CharField(max_length=50)),
            ],
        ),
    ]
