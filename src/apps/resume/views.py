from django.views.generic import ListView

from apps.resume.models import Project
from apps.resume.models import ResumePage


class IndexView(ListView):
    template_name = "resume/index.html"
    model = Project

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["resume_list"] = ResumePage.objects.all()
        return context
