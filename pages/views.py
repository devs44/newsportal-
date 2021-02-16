from django.shortcuts import render
from .models import Trending


# Create your views here.
def home(request):
    trendings = Trending.objects.all()
    return render(request, 'pages/home.html',{'trendings':trendings})

def about(request):

    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')
