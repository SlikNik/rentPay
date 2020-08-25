from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    firstname = models.CharField(max_length=120, blank=True, null=True)
    lastname = models.CharField(max_length=120, blank=True, null=True)
    displayname = models.CharField(max_length=120, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
    REQUIRED_FIELDS = ['firstname', 'lastname', 'age', 'homepage']

    def __str__(self):
        return self.username
