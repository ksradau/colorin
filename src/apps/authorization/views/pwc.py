from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


class PwcView(PasswordChangeView):
    template_name = "authorization/pwc_form.html"
    success_url = reverse_lazy("authorization:pwc_done")
