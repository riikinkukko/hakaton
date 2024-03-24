from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'name': 'username',},))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'name': 'password',},))

    class Meta:
        model = User
        fields = ['username', 'password']

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['id', 'user_id', 'url_to_file', 'tags']
        widgets = {
            "user_id": forms.HiddenInput(),
        }

class UploadVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['id', 'user_id', 'url_to_file', 'tags']
        widgets = {
            "user_id": forms.HiddenInput(),
        }