from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.homeview.as_view(), name='homepage'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.RegisterView.as_view(), name='signup'),
    # path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/signup/rescue/', views.RescueSignUpView.as_view(), name='rescue_signup'),
    path('accounts/signup/pound/', views.PoundSignUpView.as_view(), name='pound_signup'),
    path('profiles/', views.ProfileList.as_view(), name='profiles'),
    path('create_profile/', views.CreateProfile.as_view(), name='create_profile'),
    path('edit_profile/', views.EditProfile.as_view(), name='edit_profile'),
    path('delete_profile/', views.DeleteProfile.as_view(), name='delete_profile'),
]