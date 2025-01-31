from django.contrib import admin
from .models import Doctor, Appointment, Payment, DeletedAppointment, DeletedUser

admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Payment)
admin.site.register(DeletedAppointment)
admin.site.register(DeletedUser)