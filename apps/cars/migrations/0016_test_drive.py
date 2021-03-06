# Generated by Django 3.2.7 on 2022-05-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_auto_20220521_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_drive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Имя', max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(help_text=255, max_length=255)),
                ('date', models.DateTimeField()),
                ('crated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Тест драйв',
                'verbose_name_plural': 'Тест Драйвы',
            },
        ),
    ]
