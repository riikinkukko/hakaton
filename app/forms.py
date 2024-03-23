from django import forms
from .models import *
from django_range_slider.fields import RangeSliderField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

month_choices = {1: 'Январь', 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
year_choices_min = []
year_choices_max = [2025]
for i in range(1990, 2025):
    year_choices_min.append(i)
    year_choices_max.append(i)

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

class MetaFilter(forms.Form):
    image_width = RangeSliderField(minimum=0, maximum=5000, step=10, label='Ширина изображения')
    image_height = RangeSliderField(minimum=0, maximum=5000, step=10, label='Высота изображения')
    min_date = forms.DateTimeField(widget=forms.SelectDateWidget(years=year_choices_min, months=month_choices), label='Изображение создано не раньше')
    max_date = forms.DateTimeField(widget=forms.SelectDateWidget(years=year_choices_max, months=month_choices), label='Изображение создано не позже')