from django.views.generic import TemplateView

from apps.colorin.models import ColorinPage


class IndexView(TemplateView):
    template_name = "colorin/index.html"

