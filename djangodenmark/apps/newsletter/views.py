from django.urls.base import reverse
from django.views.generic.base import RedirectView
from django_consent import models
from django_consent.views import ConsentConfirmationSentView
from django_consent.views import ConsentCreateView


class Index(RedirectView):

    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        source = models.ConsentSource.objects.all().first()
        if not source:
            source = models.ConsentSource.objects.create(
                source_name="Auto-created default newsletter"
            )
        return reverse("newsletter:signup", kwargs={"source_id": source.id})


class ConsentCreateView(ConsentCreateView):
    template_name = "signup.html"

    def get_success_url(self):
        return reverse(
            "demo:signup_confirmation", kwargs={"source_id": self.consent_source.id}
        )


class ConsentConfirmationSentView(ConsentConfirmationSentView):
    pass
