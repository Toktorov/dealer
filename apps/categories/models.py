from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", help_text="Внедорожники")
    category_image = models.ImageField(upload_to = "category_image/", verbose_name="Изображение категории")
    slug = models.SlugField(max_length=255, verbose_name="slug")

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"