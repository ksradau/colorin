from django.views.generic import TemplateView, ListView
from django.shortcuts import render
import requests
#from apps.colorin.forms import ImageForm
from django.contrib.auth import get_user_model

from django.views.generic.edit import FormView
from .forms import FileFieldForm
from apps.colorin.models import UploadedPhoto

User = get_user_model()


class IndexView(TemplateView):
    template_name = "colorin/index.html"


class AllPhotoView(ListView):
    model = UploadedPhoto
    template_name = "colorin/all.html"

    def get_queryset(self):
        return UploadedPhoto.objects.filter(user_id=self.request.user.id)


class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'colorin/add.html'
    success_url = '/colorin/all/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                uploaded = UploadedPhoto(user_id=request.user.id, photo=f)
                uploaded.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)