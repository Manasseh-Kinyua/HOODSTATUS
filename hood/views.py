from django.shortcuts import render, redirect
from .models import Neighborhood
from .forms import HoodForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.error(request, 'Username or Password does not exist')
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