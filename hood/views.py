from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'hood/index.html', context)

def hoods(request):
    context = {}
    return render(request, 'hood/hoods.html', context)
