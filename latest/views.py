from django.shortcuts import render
from .models import Latest
# Create your views here.
def latest(request):
    latests = Latest.objects.all()
    return render(request, 'latest/latest.html', {'latests':latests})
