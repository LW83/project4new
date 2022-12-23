from rest_framework import serializers
from .models import Profile, Booking


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileBookingSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Booking
        fields = "__all__"
