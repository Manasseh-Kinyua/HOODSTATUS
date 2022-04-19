from django.shortcuts import render, redirect
from .models import Neighborhood, Profile
from .forms import HoodForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def loginpage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
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
    context = {
        "page": page
    }
    return render(request, 'hood/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def registerUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'An error occurred during registration')
    context = {
        "form": form,
    }
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

@login_required(login_url='/login')
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

def profile(request):

    context = {
        'profile': Profile.objects.filter(user= request.user)
    }
    return render(request, 'hood/profile.html', context)