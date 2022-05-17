from django.shortcuts import render
from apps.settings.models import Setting
from apps.cars.models import Car
from apps.categories.models import Category

# Create your views here.
def index(request):
    home = Setting.objects.latest('id')
    cars = Car.objects.all()
    random_cars = Car.objects.all().order_by('?')
    categories = Category.objects.all()
    context = {
        'home' : home,
        'cars' : cars,
        'random_cars' : random_cars,
        'categories' : categories,
    }
    return render(request, 'index.html', context)