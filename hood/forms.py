from dataclasses import fields
from django.forms import ModelForm
from .models import Neighborhood

class HoodForm(ModelForm):
    class Meta:
        model = Neighborhood
        fields = '__all__'