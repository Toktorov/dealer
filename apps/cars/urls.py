from django.urls import path 
from apps.cars.views import car_detail

urlpatterns = [
    path('car/<str:slug>', car_detail, name = "car_detail"),
]