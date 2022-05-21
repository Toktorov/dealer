from django.shortcuts import render
from apps.categories.models import Category
from apps.cars.models import Car
from apps.settings.models import Setting

# Create your views here.
def category_detail(request, slug):
    category = Category.objects.get(slug = slug)
    home = Setting.objects.latest('id')
    cars = Car.objects.all()
    context = {
        'home' : home, 
        'category' : category,
        'cars' : cars,
    }
    return render(request, 'category_detail.html', context)