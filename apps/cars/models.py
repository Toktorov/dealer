from django.db import models

# Create your models here.
class Brand(models.Model):
    brand_title = models.CharField(max_length=255, verbose_name="Название", help_text="Mersedes")

    def __str__(self):
        return self.brand_title

    class Meta:
        verbose_name = "Название машины"
        verbose_name = "Название машины"


class Fuel(models.Model):
    fuels = models.CharField(max_length=100, verbose_name="Тип топлива", help_text="Бензин")

    def __str__(self):
        return self.fuels

    class Meta:
        verbose_name = "Тип топлива"
        verbose_name = "Типы топлива"

class Transmission(models.Model):
    type_transmission = models.CharField(max_length=255, verbose_name="Тип коробки передач")
    
    def __str__(self):
        return self.type_transmission

    class Meta:
        verbose_name = "Тип коробки передач"
        verbose_name = "Типы коробок передач"

class DriveType(models.Model):
    type_drive = models.CharField(max_length=255, verbose_name="Привод машины", help_text="Передний")

    def __str__(self):
        return self.type_drive

    class Meta:
        verbose_name = "Тип привода"
        verbose_name = "Типы приводов"

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Название машины", help_text="Mersedes")
    mileage = models.PositiveBigIntegerField(default=0, verbose_name="Пробег", help_text="120999")
    fuel_type = models.ForeignKey(Fuel, on_delete=models.CASCADE, related_name="car_fuel_type", verbose_name="Тип топлива")
    year = models.PositiveBigIntegerField(default=2000, verbose_name="Год выпуска", help_text="2000")
    drive_type = models.ForeignKey(DriveType, on_delete=models.CASCADE, verbose_name="Привод машины", help_text="Передний")
    color = models.CharField(max_length=255, verbose_name="Цвет машины", help_text="Черный")
    color_interior = models.CharField(max_length=255, verbose_name="Цвет интерьера", help_text="Молочный")
    vin = models.CharField(max_length=255, verbose_name="VIN номер", help_text="JTJHY7AX6H42")
    engine = models.CharField(max_length=255, verbose_name="Двигатель", help_text="V8 4.7")

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"