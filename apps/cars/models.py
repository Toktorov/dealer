from unicodedata import category
from django.db import models
from apps.categories.models import Category

# Create your models here.
class Brand(models.Model):
    brand_title = models.CharField(max_length=255, verbose_name="Бренд", help_text="Mersedes")
    slug = models.SlugField(max_length=255, verbose_name="Slug", help_text="bmw")

    def __str__(self):
        return self.brand_title

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренд"

class CarModel(models.Model):
    title = models.CharField(max_length=255, verbose_name="Модель машины", help_text="GLS 63")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="car_brand", verbose_name="Бренд")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Модель машины"
        verbose_name_plural = "Модель машин"


class Fuel(models.Model):
    fuels = models.CharField(max_length=100, verbose_name="Тип топлива", help_text="Бензин")

    def __str__(self):
        return self.fuels

    class Meta:
        verbose_name = "Тип топлива"
        verbose_name_plural = "Типы топлива"

class Transmission(models.Model):
    type_transmission = models.CharField(max_length=255, verbose_name="Тип коробки передач")
    
    def __str__(self):
        return self.type_transmission

    class Meta:
        verbose_name = "Тип коробки передач"
        verbose_name_plural = "Типы коробок передач"

class DriveType(models.Model):
    type_drive = models.CharField(max_length=255, verbose_name="Привод машины", help_text="Передний")

    def __str__(self):
        return self.type_drive

    class Meta:
        verbose_name = "Тип привода"
        verbose_name_plural = "Типы приводов"

class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Тип машины", related_name="car_category", null = True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Название машины", help_text="Mersedes", related_name="cars_brand")
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="car_model", verbose_name="Модель")
    car_image = models.ImageField(upload_to = "car_image/", verbose_name="Фотография автомобиля")
    mileage = models.PositiveBigIntegerField(default=0, verbose_name="Пробег", help_text="120999")
    fuel_type = models.ForeignKey(Fuel, on_delete=models.CASCADE, related_name="car_fuel_type", verbose_name="Тип топлива")
    year = models.PositiveBigIntegerField(default=2000, verbose_name="Год выпуска", help_text="2000")
    drive_type = models.ForeignKey(DriveType, on_delete=models.CASCADE, verbose_name="Привод машины", help_text="Передний")
    color = models.CharField(max_length=255, verbose_name="Цвет машины", help_text="Черный")
    color_interior = models.CharField(max_length=255, verbose_name="Цвет интерьера", help_text="Молочный")
    vin = models.CharField(max_length=255, verbose_name="VIN номер", help_text="JTJHY7AX6H42")
    engine = models.CharField(max_length=255, verbose_name="Двигатель", help_text="V8 4.7")
    price = models.PositiveBigIntegerField(verbose_name="Цена", help_text=1200000)
    transmission = models.ForeignKey(Transmission,on_delete=models.CASCADE,verbose_name="КОРОБКА ПЕРЕДАЧ",help_text="МЕХАНИКА")
    NEW_OR_OLD_CHOICE = (
        ('Старый', 'Старый'),   
        ('Новый', 'Новый')
    )
    new_or_old = models.CharField(choices=NEW_OR_OLD_CHOICE, max_length=255, verbose_name="Состояние машины", default="Новый")
    slug = models.SlugField(max_length=255, verbose_name="Слаг")

    def __str__(self):
        return f"{self.brand}, {self.model}, {self.category}"

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"