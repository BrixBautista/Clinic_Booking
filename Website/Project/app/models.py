from django.db import models
from django.contrib.auth.models import User


# Doctor model remains the same but linked to a User
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link doctor to User
    specialty = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    available = models.BooleanField(default=True)  # Doctor's availability for appointments

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name} ({self.specialty})"


# Appointment model linked to User (patient) and Doctor
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # Doctor for the appointment
    patient = models.ForeignKey(User, on_delete=models.CASCADE)  # Patient is a User
    appointment_date = models.DateTimeField()
    reason = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.user.last_name} on {self.appointment_date}"


# Payment model linked to Appointment and User (patient)
class Payment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)  # Link to Appointment
    patient = models.ForeignKey(User, on_delete=models.CASCADE)  # Payment made by a patient
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_on = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, default="Cash")  # Cash-only payment method

    def __str__(self):
        return f"Payment of {self.amount} for Appointment {self.appointment.id}"


# Deleted Appointment model linked to User and Appointment
class DeletedAppointment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)  # Which appointment was deleted
    patient = models.ForeignKey(User, on_delete=models.CASCADE)  # The patient who had the appointment
    deleted_at = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()  # Reason why the appointment was deleted

    def __str__(self):
        return f"Deleted Appointment {self.appointment.id} on {self.deleted_at}"


# Deleted User model linked to User (patient)
class DeletedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who was deleted
    deleted_at = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()  # Reason for deleting the user

    def __str__(self):
        return f"Deleted User {self.user.username} on {self.deleted_at}"