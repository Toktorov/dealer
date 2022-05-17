from django.shortcuts import render
from apps.cars.models import Car
from apps.settings.models import Setting

# Create your views here
def car_detail(request, slug):
    home = Setting.objects.latest('id')
    car = Car.objects.get(slug = slug)
    context = {
        'home' : home, 
        'car' : car,
    }
    return render(request, 'car_detail.html', context)