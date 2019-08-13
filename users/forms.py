from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#New user form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Update existing user form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email',]

#Update logged user profile
class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Profile
        fields = ['image']
       
        