from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Tag(models.Model):
    text = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return "Tag #%s" % (self.text)

class Request(models.Model):
    text = models.CharField(max_length=500, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    # tags
    tags = models.ManyToManyField(Tag)

    def getDict(self):
        return {'id': self.id, 'text': self.text, 'name': self.name, 'user': self.user.username,
                'latitude': self.latitude, 'longitude': self.longitude}

    def __unicode__(self):
        return "Request #%s" % (self.text)

