from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alternative_first_name = models.CharField(max_length=150, blank=True)
    alternative_last_name = models.CharField(max_length=150, blank=True)
