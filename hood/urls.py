from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.loginpage, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('register', views.registerUser, name = 'register'),
    path('', views.index, name = 'index'),
    path('hoods/', views.hoods, name = 'hoods'),
    path('hood/<str:pk>/', views.hood, name = 'hood'),
    path('add-hood/', views.add_hood, name = 'add'),
    path('profile/', views.profile, name = 'profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)