from django.shortcuts import render
from apps.cars.models import Car, Brand
from apps.settings.models import Setting
from apps.categories.models import Category
from django.db.models import Q

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

def car_search(request):
    cars = Car.objects.all()
    categories = Category.objects.all()
    brand = Brand.objects.all()
    qury_obj = request.GET.get('key')
    if qury_obj is not None:
        brand = Brand.objects.filter(Q(brand_title__icontains = qury_obj))
        # categories = Category.objects.filter(Q(title__icontains = qury_obj))
        # cars = Car.objects.filter(Q(vin__icontains = qury_obj))
    context = {
        'cars' : cars,
        'qury_obj' : qury_obj,
        'categories' : categories,
        'brand' : brand,
    } 
    return render(request, 'car_search.html', context)