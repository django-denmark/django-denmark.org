from django.db import models

# Create your models here.

class MeetupEvent(models.Model):
    title      =  models.CharField(max_length=180)
    date       =  models.DateField()
    start_time = models.TimeField(help_text='Starts at')
    end_time   = models.TimeField(help_text='Finishes at')
    venue      =   models.CharField(max_length=200)

    def __str__(self):
        return self.date.strftime("%B %d, %Y")