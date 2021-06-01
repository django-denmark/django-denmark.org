from django.db import models

# Create your models here.

# All fields, Event should contain with string conversion

class Event(models.Model):
    eventTitle = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=145)
    description = models.TextField()
    eventUrl = models.CharField(max_length = 100)
    eventImage = models.ImageField(upload_to = 'images/', null = True)
  
    
    def __str__(self):
        return '{} {} {} {} {}'.format(self.eventTitle, self.date, self.location, self.description, self.eventUrl)
