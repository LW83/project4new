from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView
from .models import User, Profile
from .forms import PoundSignUpForm, RescueSignUpForm, ProfileForm

# Create your views here.
class homeview(TemplateView):
    template_name = 'home.html'


class RegisterView(TemplateView):
    template_name = 'signup.html'


# class LoginView(TemplateView):
    # template_name = 'login.html'


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
                # "viewer_access": check_viewer_exists(request)
            }
        )

    def post(self, request, *args, **kwargs):
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            create_profile = profile_form.save(commit=False)
            create_profile.creator = request.user
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
                # "viewer_access": check_viewer_exists(request)
            }
        )


# class CreatorProfile(LoginRequiredMixin, View):
#     """
#     Class to display pages belonging to logged in user.
#     """
#     def get(self, request):
#         creator_pages = Page.objects.filter(creator=request.user) \
#                         .values_list('title', flat=True)
#         creator_page_list = Page.objects.filter(title__in=creator_pages)

#         return render(
#             request,
#             "creator_profile.html",
#             {
#                 "creator_page_list": creator_page_list,
#                 "viewer_access": check_viewer_exists(request)
#             }
#         )

# class ViewerProfile(LoginRequiredMixin, View):
#     """
#     Class to display pages assigned to logged in viewer.
#     """
#     def get(self, request):
#         v_pages = ViewerAccess.objects.filter(viewer_email=request.user.email)\
#                   .values_list('allowed_page', flat=True)
#         viewer_page_list = Page.objects.filter(slug__in=v_pages)

#         return render(
#             request,
#             "viewer_profile.html",
#             {
#                 "viewer_page_list": viewer_page_list,
#                 "viewer_access": check_viewer_exists(request)
#             }
#         )