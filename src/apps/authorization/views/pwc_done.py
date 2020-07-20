from django.contrib.auth.views import PasswordChangeDoneView


class PwcDoneView(PasswordChangeDoneView):
    template_name = "authorization/pwc_done.html"
