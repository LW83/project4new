from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_pound = models.BooleanField('pound status', default=False)
    is_rescue = models.BooleanField('rescue status', default=False)