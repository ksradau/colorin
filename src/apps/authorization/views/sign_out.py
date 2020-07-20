from django.contrib.auth.views import LogoutView


class SignOutView(LogoutView):
    template_name = "authorization/signed_out.html"
