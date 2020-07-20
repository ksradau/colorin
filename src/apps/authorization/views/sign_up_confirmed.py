from django.views.generic import TemplateView


class SignUpConfirmedView(TemplateView):
    template_name = "authorization/sign_up_confirmed.html"
