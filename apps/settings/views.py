from django.shortcuts import render
from apps.settings.models import Setting

# Create your views here.
def index(request):
    home = Setting.objects.latest('id')
    context = {
        'home' : home
    }
    return render(request, 'index.html', context)