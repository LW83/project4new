from django.contrib.auth.forms import UserCreationForm
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from phonenumber_field.formfields import PhoneNumberField
from .models import User, Profile, Booking


# Form to create pound user
# Based on code from https://simpleisbetterthancomplex.com/
class PoundSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "pound_official_name", "county", "password1",
                  "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_pound = True
        user.extra_field = self.cleaned_data["pound_official_name"]
        user.extra_field = self.cleaned_data["county"]
        if commit:
            user.save()
        return user


# Form to create rescue user
# Based on code from https://simpleisbetterthancomplex.com/
class RescueSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "rescue_official_name", "county", "password1",
                  "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_rescue = True
        user.extra_field = self.cleaned_data["rescue_official_name"]
        user.extra_field = self.cleaned_data["county"]
        if commit:
            user.save()
        return user


# Form for pound to create profile of dog
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('dog_breed', 'gender', 'approx_age', 'neutered',
                  'microchipped', 'circumstance', 'pound_entry_date',
                  'hold_date', 'status', 'urgency',)
        widgets = {
            'pound_entry_date': DatePickerInput(),
            'hold_date': DatePickerInput(),
        }

        """
        Based on code from keelback-code - out-proud
        """
        def form_valid(self, form):
            form.instance.created_by = self.request.user
            return super().form_valid(form)


# Form for rescue to create booking against a profile
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('collection_date', 'phone_number')
        help_texts = {
            'collection_date': ('Please enter in format YYYY-MM-DD'),
            'phone_number': ('Please enter in the format CountryCodePhoneNumber e.g. +353871234567')
        }
        widgets = {
            'collection_date': DatePickerInput(),
        }
