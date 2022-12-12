from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile

class PoundSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_pound = True
        if commit:
            user.save()
        return user


class RescueSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_rescue = True
        if commit:
            user.save()
        return user
