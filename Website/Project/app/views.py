from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import DeletedUser, Appointment, DeletedAppointment



# Create your views here.

class HomeView(TemplateView):
    template_name =  'app/home.html'

class ContactView(TemplateView):
    template_name =  'app/contact.html'

class LOGINPAGEView(LoginView):
    template_name =  'app/LOGINPAGE.html'

class SIGNUPPAGEView(TemplateView):
    template_name = 'app/SIGNUPPAGE.html'  # Path to the signup template

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()  # Create a new empty form
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)  # Get the posted form data
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in after successful sign-up
            return redirect('home')  # Redirect to home page after sign-up
        return self.render_to_response({'form': form})  # If form is invalid, re-render the form

# FOr managing User account
class UserPageView(TemplateView):
    template_name = 'app/UserPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Current logged-in user

        # Form for editing user data
        context['form'] = UserChangeForm(instance=self.request.user)

        return context

    def post(self, request, *args, **kwargs):
        if 'edit' in request.POST:
            form = UserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('UserPage')  # Redirect to user page after saving changes
        elif 'delete' in request.POST:
            user = request.user

            self.delete_user_appointments(user)


            self.delete_user_data(user)

            # Step 3: Delete the user and log them out
            user.delete()  # Delete user from the database
            logout(request)  # Log the user out
            return redirect('home')  # Redirect to the homepage after logout

        return super().post(request, *args, **kwargs)

    def delete_user_appointments(self, user):
        # Move appointments to DeletedAppointment table
        appointments = Appointment.objects.filter(patient=user)
        for appointment in appointments:
            DeletedAppointment.objects.create(
                appointment=appointment,
                patient=user,
                reason="Account deletion"
            )

    def delete_user_data(self, user):
        # Move user to DeletedUser table
        DeletedUser.objects.create(
            user=user,
            reason="Account deletion"
        )


class appointmentsPageView(TemplateView):
    template_name =  'app/appointments.html'