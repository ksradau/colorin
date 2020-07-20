from django.views.generic import TemplateView

from apps.colorin.models import ColorinPage


class IndexView(TemplateView):
    template_name = "colorin/index.html"

    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data(**kwargs)

        info = ColorinPage.objects.first()
        if info is not None:
            ctx = {
                "title": info.title,
                "description": info.description,
                "h1": info.h1,
                "university": info.university,
                "text": info.text,
            }

            ctx.update(parent_ctx)

            return ctx
