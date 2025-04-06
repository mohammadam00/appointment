from django.urls import path
from .views import AppointmentTime, AppointmentDayView ,CreateAppointment

app_name = 'appointment'

urlpatterns = [
    path('day', AppointmentDayView.as_view(), name='day'),
    path('time/<int:pk>', AppointmentTime.as_view(), name='time'),
    path('create/', CreateAppointment.as_view(), name='create'),
]
