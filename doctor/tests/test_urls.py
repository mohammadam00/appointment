from rest_framework.test import APITestCase
from doctor.models import Doctor
from django.urls import reverse, resolve
from doctor.views import DoctorDetailView, DoctorListView


class DoctorListUrlTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.doctor = Doctor.objects.create(name='hesam', education='dr', specialist='1234')

    def test_doctor_list_url(self):
        url = reverse('doctor:list')
        self.assertEqual(resolve(url).func.view_class, DoctorListView)

    def test_doctor_detail_url(self):
        url = reverse('doctor:detail', args=[self.doctor.pk])
        self.assertEqual(resolve(url).func.view_class, DoctorDetailView)


