from django import forms
from .models import *


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