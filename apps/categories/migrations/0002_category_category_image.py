# Generated by Django 3.2.7 on 2022-05-17 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default=1, upload_to='category_image/', verbose_name='Изображение категории'),
            preserve_default=False,
        ),
    ]
