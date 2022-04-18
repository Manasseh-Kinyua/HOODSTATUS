from django.shortcuts import render
from .models import Neighborhood

# Create your views here.
def index(request):
    context = {}
    return render(request, 'hood/index.html', context)

def hoods(request):
    hoods = Neighborhood.objects.all()
    context = {
        "hoods": hoods,
    }
    return render(request, 'hood/hoods.html', context)
