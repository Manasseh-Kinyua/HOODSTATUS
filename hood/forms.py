from dataclasses import fields
from django.forms import ModelForm
from .models import Neighborhood, Post

class HoodForm(ModelForm):
    class Meta:
        model = Neighborhood
        fields = '__all__'

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'