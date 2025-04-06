from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from appointment.views import AppointmentDayView, CreateAppointment, AppointmentTime
from appointment.models import AppointmentDay, Appointment
from doctor.models import Doctor


class TestAppointmentUrls(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.Appointment_day = AppointmentDay.objects.create(date='2000-12-12')
        cls.doctor = Doctor.objects.create(name='hesam', specialist='brain', education='dr')
        cls.appointment = Appointment.objects.create(name='mohamad', phone='1234', doctor=cls.doctor,
                                                     day=cls.Appointment_day, time='12:00')

    def test_appointment_day_url(self):
        url = reverse('appointment:day')
        self.assertEqual(resolve(url).func.view_class,AppointmentDayView)

    def test_appointment_time(self):
        url = reverse('appointment:time', args=[self.appointment.pk])
        self.assertEqual(resolve(url).func.view_class, AppointmentTime)

    def test_create_appointment(self):
        url = reverse('appointment:create')
        self.assertEqual(resolve(url).func.view_class, CreateAppointment)
