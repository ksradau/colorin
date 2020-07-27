from django.views.generic import TemplateView
from django.shortcuts import render
from apps.colorin.forms import ImageForm


class IndexView(TemplateView):
    template_name = "colorin/index.html"


class AllPhotoView(TemplateView):
    template_name = "colorin/all.html"


def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'colorin/add.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'colorin/add.html', {'form': form})