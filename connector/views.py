from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator # Test & delete
from django.views.generic import (View, CreateView, UpdateView, DeleteView,
                                  TemplateView, ListView)
from django.urls import reverse, reverse_lazy  # Can probably delete
from itertools import chain  # Can probably delete

from .models import User, Profile, Booking
from .forms import PoundSignUpForm, RescueSignUpForm, ProfileForm, BookingForm
from .serializers import ProfileSerializer, ProfileBookingSerializer # Test & delete
from .decorators import rescue_required, pound_required # Test & delete


# View to display homepage
class homeview(TemplateView):
    template_name = 'home.html'


# View to display Sign Up User options
class RegisterView(TemplateView):
    template_name = 'signup.html'


# View to display sign up form for pound user
class PoundSignUpView(CreateView):
    model = User
    form_class = PoundSignUpForm
    template_name = 'signuppage.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'pound'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profiles')


# View to display sign up form for rescue user
class RescueSignUpView(CreateView):
    model = User
    form_class = RescueSignUpForm
    template_name = 'signuppage.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'rescue'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profiles')


def rescue_check(user):
    return user.is_rescue


def pound_check(user):
    return user.is_pound


# View to display all dogs listed that have a status of on hold or available
class ProfileList(LoginRequiredMixin, ListView):
    model = Profile
    queryset = Profile.objects.filter(status=0) | Profile.objects.filter(status=1)
    context_object_name = 'profiles'
    template_name = 'profiles.html'
    paginate_by = 25


# View to display for pound user to create a dog profile
class CreateProfile(UserPassesTestMixin, CreateView):

    def test_func(self):
        return self.request.user.is_pound
    
    def get(self, request, *args, **kwargs):

        return render(
            request,
            "create_profile.html",
            {
                "profile_form": ProfileForm,
            }
        )

    def post(self, request, *args, **kwargs):
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            create_profile = profile_form.save(commit=False)
            create_profile.pound = request.user
            create_profile.save()
            messages.success(request, 'Profile created successfully.')
            return redirect('profiles')
        else:
            messages.error(request, 'Profile not saved, please try again.')
            profile_form = ProfileForm()

        return render(
            request,
            "create_profile.html",
            {
                "profile_form": profile_form,
            }
        )


# View to display for pound user to edit a dog profile
class EditProfile(UserPassesTestMixin, UpdateView):

    def test_func(self):
        return self.request.user.is_pound

    def get(self, request, id):
        profile_to_edit = get_object_or_404(Profile, id=id)
        edit_profile_form = ProfileForm(instance=profile_to_edit)
        if profile_to_edit.pound == request.user:
            return render(
                request,
                "edit_profile.html",
                {
                    "edit_profile_form": edit_profile_form,
                }
            )
        else:
            return redirect('profiles')

    def post(self, request, id):
        profile_to_edit = get_object_or_404(Profile, id=id)
        edit_profile_form = ProfileForm(
                         request.POST, request.FILES, instance=profile_to_edit)
        if profile_to_edit.pound == request.user:
            if edit_profile_form.is_valid():
                edit_profile_form.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('profiles')
            else:
                messages.error(request,
                               'Profile update unsuccessful,'
                               'please try again.')
                return redirect('profiles')


# View to display for pound user to delete a dog profile
class DeleteProfile(UserPassesTestMixin, DeleteView):

    def test_func(self):
        return self.request.user.is_pound

    def get(self, request, id):
        profile_to_delete = get_object_or_404(Profile, id=id)
        if profile_to_delete.pound == self.request.user:
            profile_to_delete.delete()
            messages.success(request, 'Profile was successfully deleted.')
            return redirect('my_current_dogs')
        else:
            messages.error(request,
                           'Profile deletion unsuccessful, please try again.')
            return redirect('my_current_dogs')


# View to display logged in users dashboard
class MyDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


# View to display current hold/available dogs for pound user
class MyProfileList(UserPassesTestMixin, ListView):
    model = Profile
    template_name = 'pound_my_current_dogs.html'
    paginate_by = 25

    def test_func(self):
        return self.request.user.is_pound

    def get_queryset(self):
        return Profile.objects.filter(
           Q(status=0) | Q(status=1),
           pound=self.request.user,
        )


# View to display historic dogs for pound user
class MyPreviousProfileList(UserPassesTestMixin, ListView):
    model = Profile
    template_name = 'pound_my_previous_dogs.html'

    def test_func(self):
        return self.request.user.is_pound

    def get_queryset(self):
        return Profile.objects.filter(
           Q(status=3) | Q(status=4) | Q(status=5) | Q(status=6) | Q(status=7),
           pound=self.request.user,
        )


# View to display current bookings for dogs for pound user
class MyBookingList(UserPassesTestMixin, ListView):
    model = Profile
    template_name = 'pound_my_bookings.html'

    def test_func(self):
        return self.request.user.is_pound

    def get_queryset(self):
        return Profile.objects.filter(
           Q(status=2),
           pound=self.request.user,
        )


# View to display current proposed bookings for dogs for pound user
class MyProposedBookingList(UserPassesTestMixin, ListView):
    model = Profile
    template_name = 'pound_my_proposed_bookings.html'

    def test_func(self):
        return self.request.user.is_pound

    def get_queryset(self):
        return Profile.objects.filter(
           Q(status=8),
           pound=self.request.user,
        )


# View to allow rescue user to create a booking request for a dog
class BookingRequest(UserPassesTestMixin, CreateView):

    def test_func(self):
        return self.request.user.is_rescue

    def get(self, request, id):
        profile_to_book = get_object_or_404(Profile, id=id)
        booking_form = BookingForm(instance=profile_to_book)

        return render(
            request,
            "create_booking.html",
            {
                "booking_form": BookingForm,
            }
        )

    def post(self, request, id):
        profile_to_book = get_object_or_404(Profile, id=id)
        booking_form = BookingForm(request.POST, request.FILES)
        if booking_form.is_valid():
            create_booking = booking_form.save(commit=False)
            create_booking.rescue = request.user
            create_booking.profile = profile_to_book
            create_booking.save()
            profile_to_book.status = 8
            profile_to_book.save()
            messages.success(request, 'Booking requested successfully.')
            return redirect('profiles')
        else:
            messages.error(request, 'Booking not saved, please try again.')
            booking_form = BookingForm()

        return render(
            request,
            "create_booking.html",
            {
                "booking_form": booking_form,
            }
        )


# View to allow pound user to accept a booking request
def AcceptBooking(request, id):
    profile_to_update = Profile.objects.get(id=id)
    if profile_to_update.pound == request.user:
        profile_to_update.status = 2
        messages.success(request, 'Booking accepted successfully.')
        profile_to_update.save()
        return redirect('my_booked_dogs')
    else:
        messages.error(request,
                       'Booking has not been accepted, please try again.')
        return redirect('my_proposed_bookings')


# View to allow user to delete/reject a booking request
class DeleteBooking(LoginRequiredMixin, DeleteView):

    def get(self, request, id):
        profile_to_update = get_object_or_404(Profile, id=id)
        booking_to_delete = profile_to_update.dog_booking.all()
        if profile_to_update.pound == self.request.user:
            booking_to_delete.delete()
            profile_to_update.status = 1
            profile_to_update.save()
            messages.success(request, 'Booking was successfully declined.')
            return redirect('my_dashboard')
        elif booking_to_delete.rescue == self.request.user:
            booking_to_delete.delete()
            profile_to_update.status = 1
            profile_to_update.save()
            messages.success(request, 'Booking was successfully declined.')
            return redirect('my_dashboard')
        else:
            messages.error(request,
                           'Booking deletion unsuccessful, please try again.')
            return redirect('my_dashboard')


# View to display current proposed bookings for dogs for rescue user
class MyRescueProposedBookingList(ListView):
    model = Profile
    template_name = 'rescue_my_proposed_bookings.html'

    def get_queryset(self):
        queryset=Booking.objects.select_related().filter(rescue=self.request.user, profile__status=8)
        return queryset


# View to display current bookings for dogs for rescue user
class MyRescueBookingList(ListView):
    model = Profile
    template_name = 'rescue_my_bookings.html'

    def get_queryset(self):
        queryset=Booking.objects.select_related().filter(rescue=self.request.user, profile__status=2)
        return queryset


# View to allow pound or user to confirm transfer to rescue
class ConfirmCollection(LoginRequiredMixin, View):

    def get(self, request, id):
        profile_to_update = get_object_or_404(Profile, id=id)
        related_booking = profile_to_update.dog_booking.all()
        if profile_to_update.pound == self.request.user:
            profile_to_update.status = 3
            messages.success(request, 'Rescue collection confirmed.')
            profile_to_update.save()
            return redirect('my_dashboard')
        elif related_booking.rescue == self.request.user:
            profile_to_update.status = 3
            messages.success(request, 'Rescue collection confirmed.')
            profile_to_update.save()
            return redirect('my_dashboard')
        else:
            messages.error(request,
                           'Rescue transfer confirmation unsuccessful,'
                           'please try again.')
            return redirect('my_dashboard')


# View to display rescued dogs for rescue user
class MyRescuedDogsList(UserPassesTestMixin, ListView):
    model = Profile
    template_name = 'rescue_my_rescued_dogs.html'
    paginate_by = 25

    def get_queryset(self):
        queryset=Booking.objects.select_related().filter(rescue=self.request.user, profile__status=3)
        return queryset

    def test_func(self):
        return self.request.user.is_rescue


# View to all rescue user to edit booking
class EditBooking(UserPassesTestMixin, UpdateView):

    def test_func(self):
        return self.request.user.is_rescue

    def get(self, request, id):
        booking_to_edit = get_object_or_404(Booking, id=id)
        edit_booking_form = BookingForm(instance=booking_to_edit)
        if booking_to_edit.rescue == request.user:
            return render(
                request,
                "edit_booking.html",
                {
                    "edit_booking_form": edit_booking_form,
                }
            )
        else:
            return redirect('my_dashboard')

    def post(self, request, id):
        booking_to_edit = get_object_or_404(Booking, id=id)
        edit_booking_form = BookingForm(
                         request.POST, request.FILES, instance=booking_to_edit)
        if booking_to_edit.rescue == request.user:
            if edit_booking_form.is_valid():
                edit_booking_form.save()
                messages.success(request, 'Booking updated successfully.')
                return redirect('my_dashboard')
            else:
                messages.error(request,
                               'Booking update unsuccessful,'
                               'please try again.')
                return redirect('my_dashboard')


# TO BE DELETED

# class DeleteBooking(DeleteView):
#     model = Booking
#     success_url = reverse_lazy('my_dashboard')
#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)


# # View to allow user to delete/reject a booking request
# def DeleteBooking(request, id):
#     profile = get_object_or_404(Profile, id=id)
#     booking_to_delete = Booking.objects.get(profile)
#     booking_to_delete.delete()
#     profile.status = 1
#     profile.save()
#     messages.success(request, 'Profile was successfully removed.')
#     return redirect('my_dashboard')


# def delete(request, id):
#   member = Members.objects.get(id=id)
#   member.delete()
#   return HttpResponseRedirect(reverse('index'))


# class MyRescueProposedBookingList(View):
#     template_name = 'rescue_my_proposed_booking.html'

#     def get(self, request):
#         query = Profile.objects.all()
#         queryset = Booking.objects.all()
#         serializer_profile = ProfileSerializer(query, many=True)
#         serializer_booking = ProfileBookingSerializer(queryset, many=True)
#         profile_booking = {'booking': serializer_booking.data}
#         print(profile_booking.items())
#         return render(request, 'rescue_my_proposed_booking.html',
#                 {'profile_booking': profile_booking,
#                 },
#                 )

# class MyRescueBookingList(View):

#     def get(self, request, *args, **kwargs):
#         profiles = Profile.objects.filter(status=2)
#         print(profiles)
        # bookings = profiles.objects.filter(Profile.dog_booking.rescue == self.request.user.id)
        # print(bookings)

        # if profiles and bookings:
        #     return render(request,
        #         "rescue_my_bookings.html",
        #         {
        #             "profiles": profiles,
        #             "bookings": bookings,
        #         },
        #     )
        # else:
        #     return redirect('my_dashboard')
        #     messages.error(request,
        #     'You do not have any current bookings.')

# View to display current proposed bookings for dogs for rescue user
# class MyRescueProposedBookingList(View):

#     def get(self, request, *args, **kwargs):
#         profiles = Profile.objects.filter(status=8)
#         bookings = Booking.objects.filter(rescue=self.request.user.id)

#         if profiles and bookings:
#             return render(request,
#                 "rescue_my_proposed_booking.html",
#                 {
#                     "profiles": profiles,
#                     "bookings": bookings,
#                 },
#             )
#         else:
#             return redirect('my_dashboard')
#             messages.error(request,
#             'You do not have any current proposed bookings.')


# View to display current proposed bookings for dogs for rescue user
# class MyRescueProposedBookingList(View):

#     def get(self, request, *args, **kwargs):
#         profiles = Profile.objects.filter(
#            Q(status=8),
#            (dog_booking.rescue==self.request.user)
#         )
#         return render(request,
#             "rescue_my_proposed_booking.html",
#             {
#                 "profiles": profiles,
#             },
#         )


# class MyRescueProposedBookingList(ListView):
#     model = Booking
#     template_name = 'rescue_my_proposed_bookings.html'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(rescue=self.request.user)

# class MyRescueProposedBookingList(ListView):
#     model = Booking
#     template_name = 'rescue_my_proposed_bookings.html'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         rescue_bookings = queryset.filter(rescue=self.request.user)
#         filtered_bookings = rescue_bookings.filter(rescue_bookings.profile.status==8)
#         return filtered_bookings 


# class MyRescueProposedBookingList(ListView):
#     model = Booking
#     template_name = 'rescue_my_bookings.html'
 
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(rescue=self.request.user)

#         def get_context_data(self, **kwargs):
#             context = super(MyRescueProposedBookingList, self).get_context_data(**kwargs)
#             context['profiles'] = Profile.objects.filter(status=8)
#             return context
    
#         return context

# class MyRescueProposedBookingList(View):

#     def get_queryset(self, request):
#             queryset = Profile.objects.filter(status=8)
#             expanded_queryset = queryset.select_related('booking').all()
#             bookings = expanded_queryset.filter(rescue=self.request.user)

#             return render(
#                 request,
#                 "rescue_my_proposed_bookings.html",
#                 {
#                     "bookings": bookings,
#                 },
#             )