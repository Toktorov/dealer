# Generated by Django 3.2.7 on 2022-05-17 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20220517_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(default=1, help_text='bmw', max_length=255, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
