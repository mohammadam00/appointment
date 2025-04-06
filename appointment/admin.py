from django.contrib import admin
from .models import AppointmentDay, Appointment


class InlineAppointment(admin.StackedInline):
    model = Appointment


@admin.register(AppointmentDay)
class AppointmentDayAdmin(admin.ModelAdmin):
    list_display = ('date',)
    inlines = (InlineAppointment,)
