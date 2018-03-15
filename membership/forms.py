from django import forms
from django.conf import settings
from django.contrib.auth import forms as auth_forms
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext


class InviteForm(forms.Form):
    invite_code = forms.CharField(
        label=_("Invite code"),
    )
    
    def clean_invite_code(self):
        invite_code = self.cleaned_data.get("invite_code", None) or ""
        invite_code = invite_code.lower()
        if invite_code not in settings.DJANGO_DENMARK_INVITE_CODES:
            raise forms.ValidationError(gettext("Invite code isn't valid"))
        return invite_code


class SignupForm(auth_forms.UserCreationForm):
    
    class Meta(auth_forms.UserCreationForm.Meta):
        fields = ("username", "email")

        