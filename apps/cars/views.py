from django.shortcuts import render
from apps.cars.models import Car
from apps.settings.models import Setting
from apps.categories.models import Category

# Create your views here
def car_detail(request, slug):
    home = Setting.objects.latest('id')
    car = Car.objects.get(slug = slug)
    random_cars = Car.objects.all().order_by('?')
    categories = Category.objects.all()
    context = {
        'home' : home, 
        'car' : car,
        'random_cars' : random_cars,
        'categories' : categories,
    }
    return render(request, 'car_detail.html', context)