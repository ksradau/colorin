from django.views.generic import TemplateView, ListView
from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.contrib.auth import get_user_model

from django.views.generic.edit import FormView
from .forms import FileFieldForm, UpdateInfoForm, DownLoadForm
from apps.colorin.models import UploadedPhoto

from apps.colorin.parsing.info import get_info
from apps.colorin.models import InstagramPhoto, InstagramProfile
import io

User = get_user_model()


class IndexView(TemplateView):
    template_name = "colorin/index.html"
    form = 'update_info'
    success_url = '/colorin/'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context.update({"some_context_value": 'blah blah blah',
                        "some_other_context_value": 'blah'})
        return context

    def update_info_form_valid(self, form):
        get_info(request)
        return form.update_info(self.request, redirect_url=self.get_success_url())

    def update_download_form_valid(self, form):
        return form.download_match(self.request, user, self.get_success_url())

    #def get(self, request, *args, **kwargs):
    #    get_info(request)
    #    return HttpResponse()


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


def download_zip(request):
    zip_io = io.BytesIO()
    with zipfile.ZipFile(zip_io, mode='w', compression=zipfile.ZIP_DEFLATED) as backup_zip:
        for file_img in match_images_list:
            backup_zip.write(file_img)

    response = HttpResponse(zip_io.getvalue(), content_type='application/x-zip-compressed')
    response['Content-Disposition'] = 'attachment; filename=%s' % 'my_zipfilename' + ".zip"
    response['Content-Length'] = zip_io.tell()

    return response
