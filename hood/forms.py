from django.db.models import fields
from .models import *
from django.forms import ModelForm
from django import forms


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_photo','contact','location','animalsranch')

class HoodForm(forms.ModelForm):
    class Meta:
        model=AnimalsRanch
        fields = ['photo','name','content','location', 'Charateristics', 'health_cell','police_hotline']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','comment','location','animalsranch']