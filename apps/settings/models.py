from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", help_text="Toyota")
    logo = models.ImageField(upload_to = "logo/", verbose_name="Логотип")
    address = models.CharField(max_length=255, verbose_name="Адрес", help_text="Ош")
    tel = models.CharField(max_length=255, verbose_name="Телефонный номер", help_text="+996772343206")
    work_time = models.CharField(max_length=255, verbose_name="Время работы", help_text="09:00 - 20:00 ПН-ПТ")

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"
