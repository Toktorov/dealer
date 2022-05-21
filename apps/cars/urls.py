from django.urls import path 
from apps.cars.views import car_detail, car_search

urlpatterns = [
    path('car/<str:slug>', car_detail, name = "car_detail"),
    path('search/', car_search, name = "car_search"),
]