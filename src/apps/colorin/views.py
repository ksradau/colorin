from django.views.generic import TemplateView

from apps.colorin.models import ColorinModel


class IndexView(TemplateView):
    template_name = "colorin/index.html"


class AllPhotoView(TemplateView):
    template_name = "colorin/all.html"
    

class AddPhotoView(TemplateView):
    template_name = "colorin/add.html"