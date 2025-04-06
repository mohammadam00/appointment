from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from account.models import User
from django.urls import reverse
from rest_framework import status


class AuthView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.phone = '1234'
        cls.password = '1234'
        cls.user = User.objects.create_user(phone=cls.phone, password=cls.password)
        refresh = RefreshToken.for_user(cls.user)
        cls.token = str(refresh.access_token)

    def test_profile_auth(self):
        url = reverse('account:profile')
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['phone'])

    def test_profile_detail_unauth(self):
        url = reverse('account:profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login(self):
        url = reverse('account:login')
        data = {
            'phone': self.phone,
            'password': self.password
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.failUnless(response.data['access'])
