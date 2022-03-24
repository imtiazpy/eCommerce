import email
from email import message
from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=False)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=False)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(max_length=500, null=True, blank=False)

    def __str__(self):
        return self.first_name
