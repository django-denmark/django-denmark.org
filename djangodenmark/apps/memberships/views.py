from django.contrib.auth.views import LoginView as AuthLoginView
from django.http.response import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls.base import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django_consent.forms import EmailConsentForm
from django_consent.views import ConsentCreateView

from . import forms


class NewsletterSignupView(ConsentCreateView):
    pass


class StartView(TemplateView):

    template_name = "memberships/start.html"

    # Balder is working on this
    def get_context_data_soon(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c["newsletter_form"] = EmailConsentForm(
            consent_source="x"  # TODO: We need a good way to seed consent such as this.
        )
        return c


class InviteView(FormView):

    form_class = forms.InviteForm
    template_name = "memberships/invite.html"

    def form_valid(self, __):
        self.request.session["invited"] = True
        return redirect("memberships:signup")


class SignupView(CreateView):

    form_class = forms.SignupForm
    template_name = "memberships/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.session["invited"]:
            return HttpResponseForbidden("You need to be invited")
        return CreateView.dispatch(self, request, *args, **kwargs)

    def get_success_url(self):
        return reverse("memberships:login")


class LoginView(AuthLoginView):

    template_name = "memberships/login.html"
