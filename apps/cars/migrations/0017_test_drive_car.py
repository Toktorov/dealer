# Generated by Django 3.2.7 on 2022-05-24 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0016_test_drive'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_drive',
            name='car',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Mashina', to='cars.car'),
            preserve_default=False,
        ),
    ]