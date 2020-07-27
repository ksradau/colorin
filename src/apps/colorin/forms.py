from django import forms
from .models import UploadedPhoto


class ImageForm(forms.ModelForm):
    class Meta:
        model = UploadedPhoto
        fields = ('photo',)
