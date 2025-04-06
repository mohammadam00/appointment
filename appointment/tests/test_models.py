from rest_framework.test import APITestCase
from appointment.models import AppointmentDay, Appointment
from django.utils.translation import gettext_lazy as _
from doctor.models import Doctor


class AppointmentDayModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.appointmentday = AppointmentDay.objects.create(date='2002-12-12')

    def test_appointment_day_field_label(self):
        field_label = self.appointmentday._meta.get_field('date').verbose_name
        self.assertEqual(field_label, _('روز'))

    def test_str_method(self):
        expected_result = self.appointmentday.date
        self.assertEqual(self.appointmentday.__str__(), expected_result)


class AppointmentModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.appointmentday = AppointmentDay.objects.create(date='2001-08-05')
        cls.doctor = Doctor.objects.create(name='hesam', specialist='dr', education='dr')
        cls.appointment = Appointment.objects.create(name='hesam', phone='1234', doctor=cls.doctor,
                                                     day=cls.appointmentday, time='09:00')

    def test_name_field_label(self):
        field_label = self.appointment._meta.get_field('name').verbose_name
        self.assertEqual(field_label, _('نام و نام خانوادگی بیمار'))

    def test_phone_field_label(self):
        field_label = self.appointment._meta.get_field('phone').verbose_name
        self.assertEqual(field_label, _('شماره تلفن'))

    def test_doctor_field_label(self):
        field_label = self.appointment._meta.get_field('doctor').verbose_name
        self.assertEqual(field_label, _('دکتر'))

    def test_day_field_label(self):
        field_label = self.appointment._meta.get_field('day').verbose_name
        self.assertEqual(field_label, _('روز'))

    def test_time_field_label(self):
        field_label = self.appointment._meta.get_field('time').verbose_name
        self.assertEqual(field_label, _('ساعت'))

    def test_str_method(self):
        expected_result = self.appointment.name
        self.assertEqual(self.appointment.__str__(), expected_result)