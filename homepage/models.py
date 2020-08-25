from django.db import models
from customUsers.models import MyUser

# Create your models here.
# class Renter(models.Model):
#     renter = models.ForeignKey(MyUser, on_delete=models.CASCADE)
#     street = models.CharField(max_length=50)
#     apt = models.CharField(max_length=50, blank=True, null=True)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     add_date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.renter