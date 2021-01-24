from django.db import models
from django.db.models import F
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class EmailConsentSources(models.Model):
    """
    A consent source always has to be present when adding email addresses. It
    should clearly specify how we imagine that the user opted in.
    
    Specific events for specific users could be captured as well, but we intend
    to start out a bit less dramatic.
    
    Notice that some consent sources may change their meaning over time. For
    instance, someone can sign up as a member and continue to receive certain
    email updates despite their membership expiring.
    
    In a different case, the consent may be implicit because the email is
    mandatory: For instance password reminders, membership confirmations,
    confirmations of website actions etc.
    """

    source_name = models.CharField(max_length=255)
    definition = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class EmailConsent(models.Model):
    """
    Specifies the consent of a user to receive emails and what source the
    consent originated from.
    
    Usually, the source will also clarify which emails we MAY send.
    """
    
    source = models.ForeignKey(EmailConsentSources)
    user = models.ForeignKey(get_user_model())
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @property
    def email(self):
        return self.user.email

    def get_valid_consent(self):
        """
        Returns all current consent (that have not opted out)
        """
        return EmailConsent.objects.exclude(
            user__optouts__consent__is_everything=True
        ).exclude(
            optouts__user=F('user')
        )


class EmailCampaign(models.Model):
    """
    For every type of email that goes out, specify:
    
    1. a name of the campaign
    2. the type of consent necessary (prefer to use existing consents and don't invent new ones)
    
    Notice that users don't opt out of a campaign, but they withdraw their
    consent from the original source of when it was given and to which we assume
    we can send the campaign.
    """
    
    name = models.CharField(max_length=255, verbose_name=_("name"))
    consent = models.ManyToManyField(EmailConsentSources)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class EmailOptOut(models.Model):
    """
    A user can opt out of different scopes, thus withdrawing their consent:
    
    * Everything
    * A specific consent
    
    Notice that for some types of emails, a user may not opt out: For instance,
    if they are members of an association and it calls its members to the
    general assembly.
    
    Setting ``consent=None`` is the same as opting out of everything.
    """

    user = models.ForeignKey(get_user_model(), related_name='optouts')
    consent = models.ForeignKey('EmailConsent', blank=True, null=True, related_name='optouts')
    is_everything = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self):
        if self.consent_id is None:
            self.is_everything = True
