from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from .models import User
from .forms import PoundSignUpForm

# Create your views here.
class homeview(TemplateView):
    template_name = 'home.html'


class RegisterView(TemplateView):
    template_name = 'account_signup.html'


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


class ProfileList(LoginRequiredMixin, generic.ListView):
    model = Profile
    queryset = Profile.objects.filter(status=0) | Profile.objects.filter(status=1)
    context_object_name = 'profiles'
    template_name = 'index.html'
    paginate_by = 50
