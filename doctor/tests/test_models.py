from rest_framework.test import APITestCase
from doctor.models import Doctor
from django.utils.translation import gettext_lazy as _


class DoctorModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.doctor = Doctor.objects.create(name='hesam', specialist='dr', education='dr')

    def test_name_field(self):
        field_label = self.doctor._meta.get_field('name').verbose_name
        self.assertEqual(field_label, _('نام و نام خانوادگی'))

    def test_specialist_field(self):
        field_label = self.doctor._meta.get_field('specialist').verbose_name
        self.assertEqual(field_label, _('تخصص'))

    def test_education_field(self):
        field_label = self.doctor._meta.get_field('education').verbose_name
        self.assertEqual(field_label, _('تحصیلات'))

    def test_str_method(self):
        expected_result = self.doctor.name
        self.assertEqual(self.doctor.__str__(), expected_result)
