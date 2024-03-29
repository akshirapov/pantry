from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.utils.translation import gettext_lazy as _

from .forms import UserRegisterForm


class UserRegisterView(CreateView):
    """
    A view for registration a new user.
    """

    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, _("Your account has been created."))
        return super().form_valid(form)


class UserLoginView(LoginView):
    """
    A view for login user.
    """

    template_name = "users/login.html"


class UserLogoutView(LogoutView):
    """
    A view for logout user.
    """

    template_name = "users/logout.html"

    def get(self, request, *args, **kwargs):
        messages.info(self.request, _("You have been logged out."))
        return super().get(self, request, *args, **kwargs)
