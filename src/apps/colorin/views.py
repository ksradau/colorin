from django.views.generic import TemplateView, ListView
from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.contrib.auth import get_user_model

from django.views.generic.edit import FormView
from .forms import FileFieldForm

from apps.colorin.parsing.info import create_profile, update_profile
from apps.colorin.models import InstagramPhoto, InstagramProfile, UploadedPhoto, EmojiPic

from django.shortcuts import redirect
import io
import zipfile
from apps.colorin.palette.get import get_palette
from apps.colorin.palette.match import match, match_emoji
import os.path
from apps.colorin.parsing.images import save_images
import random
import string
import tempfile
from django.core import files
from apps.colorin.parsing.emoji_parsing import add_emoji

User = get_user_model()


class IndexView(TemplateView):
    template_name = "colorin/index.html"

    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data(**kwargs)

        inst_profile = InstagramProfile.objects.filter(user_id=self.request.user.id).first()

        if inst_profile is not None:
            ctx = {"inst_biography": inst_profile.inst_biography,
                       "inst_full_name": inst_profile.inst_full_name,
                       "inst_profile_pic": inst_profile.inst_profile_pic,
                       "inst_theme_color": inst_profile.inst_theme_color[1:-1],
                       "instagram_photo_list": InstagramPhoto.objects.filter(user_id=self.request.user.id),
                       "uploaded_photo_match_list": UploadedPhoto.objects.filter(user_id=self.request.user.id, is_match=True),
                       }

            if inst_profile.emoji_match_list is not None:
                ctx["emoji_match_list"] = eval(inst_profile.emoji_match_list)

            ctx.update(parent_ctx)
            return ctx


class AllPhotoView(ListView):
    model = UploadedPhoto
    template_name = "colorin/all.html"

    def get_queryset(self):
        return UploadedPhoto.objects.filter(user_id=self.request.user.id)


class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'colorin/add.html'
    success_url = '/colorin/all/'
    number_of_colors = 6
    
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            number_of_colors = 6
            for f in files:
                palette = get_palette(f, number_of_colors)
                dominant = palette[0]
                uploaded = UploadedPhoto(user_id=request.user.id, 
                                         photo=f, 
                                         palette=palette,
                                         dominant=dominant)
                uploaded.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def download_zip(request):
    zip_io = io.BytesIO()
    match_images_list = UploadedPhoto.objects.filter(user_id=request.user.id, is_match=True).all()
    with zipfile.ZipFile(zip_io, mode='w', compression=zipfile.ZIP_DEFLATED) as backup_zip:
        for file_img in match_images_list:

            request = requests.get(file_img.photo.url, stream=True)
            lf = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
            for block in request.iter_content(1024 * 8):
                if not block:
                    break
                lf.write(block)
            lf.seek(0)
            backup_zip.write(lf.name)

    response = HttpResponse(zip_io.getvalue(), content_type='application/x-zip-compressed')
    response['Content-Disposition'] = 'attachment; filename=%s' % 'last_zip_match' + ".zip"
    response['Content-Length'] = zip_io.tell()

    return response


def update_info(request):
    update_profile(request)
    response = redirect('/colorin/')
    return response


def update_info_first(request):
    create_profile(request)
    response = redirect('/colorin/')
    return response


def match_images(request):
    match(request)
    response = redirect('/colorin/')
    return response


def add_emoji_to_db(request):
    add_emoji(request)
    response = redirect('/colorin/')
    return response


def match_emoji_pics(request):
    match_emoji(request)
    response = redirect('/colorin/')
    return response
