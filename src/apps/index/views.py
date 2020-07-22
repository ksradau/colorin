from django.views.generic import TemplateView

from apps.index.models import UserInfo


class IndexView(TemplateView):
    template_name = "index/index.html"
