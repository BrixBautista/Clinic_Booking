from django.urls import path
from .views import HomeView, ContactView, LOGINPAGEView, SIGNUPPAGEView

urlpatterns = [
    path('',HomeView.as_view(), name = 'home'),
    path('/contact',ContactView.as_view(), name = 'contact'),
    path('/LOGINPAGE',LOGINPAGEView.as_view(), name = 'LOGINPAGE'),
    path('/SIGNUPPAGE',SIGNUPPAGEView.as_view(), name = 'SIGNUPPAGE'),

]