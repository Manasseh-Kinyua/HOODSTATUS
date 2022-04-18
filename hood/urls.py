from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('hoods/', views.hoods, name = 'hoods'),
    path('hood/<str:pk>/', views.hood, name = 'hood'),
    path('add-hood/', views.add_hood, name = 'add')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)