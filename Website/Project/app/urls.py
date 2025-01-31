from django.urls import path
from django.contrib.auth import views as auth_views  # Import the LoginView
from . import views
from .views import (HomeView, ContactView, LOGINPAGEView,
                    SIGNUPPAGEView, UserPageView, appointmentsPageView)

urlpatterns = [
    path('',HomeView.as_view(), name = 'home'),
    path('/contact',ContactView.as_view(), name = 'contact'),
    path('/LOGINPAGE',LOGINPAGEView.as_view(), name = 'LOGINPAGE'),
    path('/SIGNUPPAGE',SIGNUPPAGEView.as_view(), name = 'SIGNUPPAGE'),
    path('/UserPage', UserPageView.as_view(), name='UserPage'),
    path('/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('/appointments', appointmentsPageView.as_view(), name='appointments'),
]