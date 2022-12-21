from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
COUNTY = ((0, "Antrim"), (1, "Armagh"), (2, "Carlow"), (3, "Cavan"), (4, "Clare"), (5, "Cork"), (6, "Derry"), (7, "Donegal"), (8, "Down"), (9, "Dublin"), (10, "Fermanagh"), (11, "Galway"), (12, "Kerry"), (13, "Kildare"), (14, "Kilkenny"), (15, "Laois"), (16, "Leitrim"), (17, "Limerick"), (18, "Longford"), (19, "Louth"), (20, "Mayo"), (21, "Meath"), (22, "Monaghan"), (23, "Offaly"), (24, "Roscommon"), (25, "Sligo"), (26, "Tipperary"), (27, "Tyrone"), (28, "Waterford"), (29, "Westmeath"), (30, "Wexford"), (31, "Wicklow"))


class User(AbstractUser):
    is_pound = models.BooleanField('pound status', default=False)
    is_rescue = models.BooleanField('rescue status', default=False)
    pound_official_name = models.CharField(max_length=150, default='To be populated', unique=False)
    rescue_official_name = models.CharField(max_length=150, default='To be populated', unique=False)
    county = models.IntegerField(choices=COUNTY, default=0)


STATUS = ((0, "Hold"), (1, "Available"), (2, "Booked"), (3, "Transferred to Rescue"), (4, "Rehomed"), (5, "Reclaimed"), (6, "PTS"), (7, "Death Natural Causes"), (8, "Booking Proposed"))
URGENCY = ((0, "Red"), (1, "Amber"), (2, "Green"))
NEUTERED = ((0, "Yes"), (1, "No"), (2, "Unknown"))
MICROCHIPPED = ((0, "Yes"), (1, "No"), (2, "Unknown"))
CIRCUMSTANCE = ((0, "Stray"), (1, "Surrender"), (2, "Seized"), (3, "Other"))
GENDER = ((0, "Male"), (1, "Female"))


class Profile(models.Model):
    profile_added = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    pound = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pound_name')
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


class Booking(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='dog_booking')
    rescue = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rescue_name')
    collection_date = models.DateField()
    phone_number = PhoneNumberField(null=False, blank=False)
    approved = models.BooleanField(default=False)
