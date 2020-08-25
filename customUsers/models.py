from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    firstname = models.CharField(max_length=120, blank=True, null=True)
    lastname = models.CharField(max_length=120, blank=True, null=True)
    displayname = models.CharField(max_length=120, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    apt = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    REQUIRED_FIELDS = ['firstname', 'lastname', 'age', 'displayname']

    def __str__(self):
        return self.username
