from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.core.validators import RegexValidator

# Create your models here.

JOBTYPE_CHOICES = (
    ("PartTime", "Part-time"),
    ("FullTime", "Full-time"),
    ("Freelancer", "Freelancer"),
    ("Internship", "Internship"),
    ("Other", "Other"),
)

class Jobpost(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None)
    jobTitle = models.CharField(max_length=60)
    jobCompanyName = models.CharField(max_length=100)
    jobDescription = models.TextField()
    jobType = models.CharField(max_length=11, choices = JOBTYPE_CHOICES)
    jobLocation = models.CharField(max_length=100)
    jobContactPerson = models.CharField(max_length=80)
    jobApplyHere = models.URLField(max_length = 100, blank=True, 
    validators=[
        RegexValidator(
            regex='[http]',
            message='Job link must include https:// or http://',
            code='invalid_url'
        ),
    ])
    
    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.user, self.jobTitle, self.jobCompanyName, self.jobDescription, self.jobType, self.jobLocation, self.jobContactPerson,self.jobContactPerson, self.jobApplyHere)

class JobpostForm(ModelForm):
    def init(self, args, **kwargs):
        super(JobpostForm, self).__init__(args, **kwargs)

    class Meta:
        model = Jobpost
        exclude = ('user',)
        fields = '__all__'
        labels = {
            "jobTitle": ("Job title"),
            "jobCompanyName": ("Company name"),
            "jobDescription": ("Describe the position"),
            "jobType": ("Job type"),
            "jobLocation": ("Location"),
            "jobContactPerson": ("Contact person"),
            "jobApplyHere": ("Insert link or mail here"),
        }
