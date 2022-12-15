from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.homeview.as_view(), name='homepage'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.RegisterView.as_view(), name='signup'),
    path('accounts/signup/rescue/', views.RescueSignUpView.as_view(), name='rescue_signup'),
    path('accounts/signup/pound/', views.PoundSignUpView.as_view(), name='pound_signup'),
    path('profiles/', views.ProfileList.as_view(), name='profiles'),
    path('create_profile/', views.CreateProfile.as_view(), name='create_profile'),
    path('<int:id>/edit_profile/', views.EditProfile.as_view(), name='edit_profile'),
    path('<int:id>/delete_profile/', views.DeleteProfile.as_view(), name='delete_profile'),
    path('my_dashboard/', views.MyDashboard.as_view(), name='my_dashboard'),
    path('my_dashboard/my_current_dogs', views.MyProfileList.as_view(), name='my_current_dogs'),
    path('my_dashboard/my_previous_dogs', views.MyPreviousProfileList.as_view(), name='my_previous_dogs'),
    path('my_dashboard/my_booked_dogs', views.MyBookingList.as_view(), name='my_booked_dogs'),
    path('my_dashboard/my_proposed_bookings', views.MyProposedBookingList.as_view(), name='my_proposed_bookings'),
]