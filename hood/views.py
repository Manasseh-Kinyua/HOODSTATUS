from django.shortcuts import render, redirect
from .models import Neighborhood
from .forms import HoodForm

# Create your views here.
def loginpage(request):
    context = {}
    return render(request, 'hood/login_register.html', context)

def index(request):
    context = {}
    return render(request, 'hood/index.html', context)

def hoods(request):
    hoods = Neighborhood.objects.all()
    context = {
        "hoods": hoods,
    }
    return render(request, 'hood/hoods.html', context)

def hood(request, pk):
    hood = Neighborhood.objects.get(id=pk)
    context = {
        "hood": hood
    }
    return render(request, 'hood/hood.html', context)

def add_hood(request):
    form = HoodForm()
    if request.method =='POST':
        form = HoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hoods')
    context = {
        "form": form
    }
    return render(request, 'hood/hood_form.html', context)