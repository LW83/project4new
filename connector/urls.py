from .views import RegisterView, homeview, PoundSignUpView, RescueSignUpView
from django.urls import path, include

urlpatterns = [
    path('', homeview.as_view(), name='homepage'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', RegisterView.as_view(), name='signup'),
    # path('accounts/login/', .as_view(), name='login'),
    path('accounts/signup/rescue/', RescueSignUpView.as_view(), name='rescue_signup'),
    path('accounts/signup/pound/', PoundSignUpView.as_view(), name='pound_signup'),
]