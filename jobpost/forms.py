from django.forms import ModelForm

from .models import Jobpost


class JobpostForm(ModelForm):
    """Form for users to add Jobpost from front end"""

    class Meta:
        model = Jobpost
        exclude = ("user",)
        fields = "__all__"
