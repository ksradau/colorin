from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from apps.colorin.parsing.info import get_info

User = get_user_model()


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


class SignUpView(FormView):
    template_name = "registration/registration.html"
    form_class = SignUpForm
    success_url = reverse_lazy("colorin:index")

    def form_valid(self, form):
        form.save()

        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]

        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        get_info(self.request)
        return super().form_valid(form)
