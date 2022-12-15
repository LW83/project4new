from django.contrib.auth.forms import UserCreationForm
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from .models import User, Profile

class PoundSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "pound_official_name", "county", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_pound = True
        user.extra_field = self.cleaned_data["pound_official_name"]
        user.extra_field = self.cleaned_data["county"]
        if commit:
            user.save()
        return user


class RescueSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "rescue_official_name", "county", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_rescue = True
        user.extra_field = self.cleaned_data["rescue_official_name"]
        user.extra_field = self.cleaned_data["county"]
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('dog_breed', 'gender', 'approx_age', 'neutered', 'microchipped', 'circumstance', 'pound_entry_date', 'hold_date', 'status', 'urgency')
        widgets = {
            'pound_entry_date':DatePickerInput(), 
            'hold_date':DatePickerInput(),
        }

        """
        From keelback-code - out-proud
        """
        def form_valid(self, form):
            form.instance.created_by = self.request.user
            return super().form_valid(form)