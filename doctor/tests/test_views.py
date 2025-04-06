from rest_framework.test import APITestCase
from doctor.models import Doctor
from django.urls import reverse
from rest_framework import status


class DoctorViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.doctor = Doctor.objects.create(name='hesam', education='dr', specialist='1234')

    def test_doctor_list_view(self):
        url = reverse('doctor:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_doctor_detail_view(self):
        url = reverse('doctor:detail', args=[self.doctor.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_doctor_add_view(self):
        url = reverse('doctor:add')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
