from django import forms
from django.forms import HiddenInput, ModelForm
from apps.colorin.models import InstagramPhoto, InstagramProfile, UploadedPhoto


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
