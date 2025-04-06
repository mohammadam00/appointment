from rest_framework import serializers
from .models import AppointmentDay, Appointment


class AppointmentDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentDay
        fields = ['id', 'date']


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'name', 'phone', 'doctor', 'day', 'time']
