# Generated by Django 3.2.7 on 2022-05-21 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_car_transmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(help_text='Mersedes', on_delete=django.db.models.deletion.CASCADE, related_name='cars_brand', to='cars.brand', verbose_name='Название машины'),
        ),
    ]
