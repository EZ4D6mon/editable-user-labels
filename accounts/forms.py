from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 


from .models import *

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
        exclude = ['tag']