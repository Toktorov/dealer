# Generated by Django 3.2.7 on 2022-05-24 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0017_test_drive_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_drive',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car'),
        ),
    ]
