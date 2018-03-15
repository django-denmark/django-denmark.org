from django.contrib.auth.views import LoginView as AuthLoginView
from django.http.response import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls.base import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView

from . import forms


class StartView(TemplateView):
    
    template_name = "membership/start.html"
    

class InviteView(FormView):
    
    form_class = forms.InviteForm
    template_name = "membership/invite.html"

    def form_valid(self, __):
        self.request.session["invited"] = True
        return redirect("membership:signup")


class SignupView(CreateView):
    
    form_class = forms.SignupForm
    template_name = "membership/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.session["invited"]:
            return HttpResponseForbidden("You need to be invited")
        return CreateView.dispatch(self, request, *args, **kwargs)

    def get_success_url(self):
        return reverse("membership:login")


class LoginView(AuthLoginView):
    
    template_name = "membership/login.html"
