from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_pound = models.BooleanField('pound status', default=False)
    is_rescue = models.BooleanField('rescue status', default=False)


STATUS = ((0, "Hold"), (1, "Available"), (2, "Booked"), (3, "Transferred to Rescue"), (4, "Rehomed"), (5, "Reclaimed"), (6, "PTS"), (7, "Death Natural Causes"))
URGENCY = ((0, "Red"), (1, "Amber"), (2, "Green"))
NEUTERED = ((0, "Yes"), (1, "No"), (2, "Unknown"))
MICROCHIPPED = ((0, "Yes"), (1, "No"), (2, "Unknown"))
CIRCUMSTANCE = ((0, "Stray"), (1, "Surrender"), (2, "Seized"), (3, "Other"))
GENDER = ((0, "Male"), (1, "Female"))

class Profile(models.Model):
    profile_added = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    pound = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dog_profiles')
    dog_breed = models.CharField(max_length=150, unique=False)
    gender = models.IntegerField(choices=GENDER, default=0)
    approx_age = models.CharField(max_length=50, unique=False)
    neutered = models.IntegerField(choices=NEUTERED, default=2)
    microchipped = models.IntegerField(choices=MICROCHIPPED, default=2)
    circumstance = models.IntegerField(choices=CIRCUMSTANCE, default=1)
    pound_entry_date = models.DateField()
    hold_date = models.DateField()
    status = models.IntegerField(choices=STATUS, default=0)
    urgency = models.IntegerField(choices=URGENCY, default=2)

    class Meta:
        ordering = ['-urgency', 'profile_added']
