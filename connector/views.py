from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView
from .models import User, Profile
from .forms import PoundSignUpForm, RescueSignUpForm, ProfileForm

# Create your views here.
class homeview(TemplateView):
    template_name = 'home.html'


class RegisterView(TemplateView):
    template_name = 'signup.html'


class PoundSignUpView(CreateView):
    model = User
    form_class = PoundSignUpForm
    template_name = 'pound_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'pound'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profiles')


class RescueSignUpView(CreateView):
    model = User
    form_class = PoundSignUpForm
    template_name = 'rescue_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'rescue'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profiles')


class ProfileList(LoginRequiredMixin, ListView):
    model = Profile
    queryset = Profile.objects.filter(status=0) | Profile.objects.filter(status=1)
    context_object_name = 'profiles'
    template_name = 'profiles.html'
    paginate_by = 50


class CreateProfile(CreateView):
    """
    Class to allow pound users to create a dog profile.
    """
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
            page_form = ProfileForm()

        return render(
            request,
            "create_profile.html",
            {
                "profile_form": profile_form,
            }
        )


class EditProfile(UpdateView):
    """
    Class to allow pound users to update a profile.
    """
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
                               'Profile update unsuccessful, please try again.')
                return redirect('profiles')


class DeleteProfile(DeleteView):

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


# class DeleteProfile(DeleteView):
#     """
#     Class to allow pound users to delete a profile.
#     """
#     def get(self, request, id):
#         profile_to_delete = get_object_or_404(Profile, id=id)
#         delete_profile_form = ProfileForm(instance=profile_to_delete)
#         if profile_to_delete.pound == request.user:
#             return render(
#                 request,
#                 "delete_profile.html",
#                 {
#                     "delete_profile_form": delete_profile_form,
#                 }
#             )
#         else:
#             return redirect('profiles')

#     def post(self, request, id):
#         profile_to_delete = get_object_or_404(Profile, id=id)
#         delete_profile_form = ProfileForm(
#                          request.POST, request.FILES, instance=profile_to_delete)
#         if profile_to_delete.pound == request.user:
#             if delete_profile_form.is_valid():
#                 delete_profile_form.save()
#                 messages.success(request, 'Profile was successfully deleted.')
#                 return redirect('profiles')
#             else:
#                 messages.error(request,
#                                'Profile deletion unsuccessful, please try again.')
#                 return redirect('profiles')


class MyDashboard(TemplateView):
    template_name = 'pound_dashboard.html'


class MyProfileList(ListView):
    model = Profile
    template_name = 'pound_my_current_dogs.html'

    def get_queryset(self):
        return Profile.objects.filter(
           Q(status=0) | Q(status=1),
           pound=self.request.user,
        )


class MyPreviousProfileList(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'pound_my_previous_dogs.html'
    
    def get_queryset(self):
        return Profile.objects.filter(
           Q(status=3) | Q(status=4) | Q(status=5) | Q(status=6) | Q(status=7),
           pound=self.request.user,
        )


class MyBookingList(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'pound_my_bookings.html'
    
    def get_queryset(self):
        return Profile.objects.filter(
           Q(status=2),
           pound=self.request.user,
        )


class MyProposedBookingList(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'pound_my_proposed_bookings.html'
    
    def get_queryset(self):
        return Profile.objects.filter(
           Q(status=8),
           pound=self.request.user,
        )