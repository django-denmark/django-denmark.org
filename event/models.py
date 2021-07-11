from django.db import models

# Create your models here.

# All fields, Event should contain with string conversion


class Event(models.Model):
    event_title = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=145)
    description = models.TextField()
    event_url = models.CharField(max_length=100)
    event_image = models.ImageField(upload_to="images/events/", null=True)

    def __str__(self):
        return "{} {} {} {} {}".format(
            self.event_title, self.date, self.location, self.description, self.event_url
        )
