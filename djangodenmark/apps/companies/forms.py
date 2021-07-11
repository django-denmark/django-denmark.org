from django.forms import ModelForm

from .models import Company


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ("user", "created_at")
        fields = "__all__"
