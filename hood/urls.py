from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('hoods/', views.hoods, name = 'hoods'),
]