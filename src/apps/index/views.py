from django.views.generic import TemplateView

from apps.index.models import MainPage
from apps.index.models import UserInfo


class IndexView(TemplateView):
    template_name = "index/index.html"

    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data(**kwargs)

        info = UserInfo.objects.first()
        info_main = MainPage.objects.first()
        if info is not None and info_main is not None:
            ctx = {
                "name": info.name,
                "greeting": info.greeting,
                "title": info_main.title,
                "description": info_main.description,
                "h1": info_main.h1,
                "about": info_main.about,
                "python_skill": info_main.python_skill,
                "django_skill": info_main.django_skill,
                "html_skill": info_main.html_skill,
                "seo_skill": info_main.seo_skill,
                "present_activities": info_main.present_activities,
            }

            ctx.update(parent_ctx)

            return ctx
