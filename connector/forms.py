from django.contrib.auth.forms import UserCreationForm
from django import forms
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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('dog_breed', 'gender', 'approx_age', 'neutered', 'microchipped', 'circumstance', 'pound_entry_date', 'hold_date', 'status', 'urgency')

        """
        From keelback-code - out-proud
        """
        def form_valid(self, form):
            form.instance.created_by = self.request.user
            return super().form_valid(form)