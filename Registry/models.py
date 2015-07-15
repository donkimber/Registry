from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Tag(models.Model):
    text = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return "Tag #%s" % (self.text)

