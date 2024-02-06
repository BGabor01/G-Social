from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase


class AuthTest(APITestCase):
    USERNAME = 'testloginuser'
    PASSWORD = 'asdasd123'
    EMAIL = 'test@login.com'

    def setUp(self):
        User.objects.create_user(username=self.USERNAME, password=self.PASSWORD,
                                 first_name='test', last_name='login', email=self.EMAIL)

    def test_registration_success(self):
        response = self.client.post(reverse('create_user'), data={
            'username': 'testuser',
            'password': 'complex_password',
            'first_name': 'test',
            'last_name': 'user',
            'email': 'test@user.com'
        })
        self.assertEqual(response.status_code, 201)

    def test_registration_fail(self):
        response = self.client.post(reverse('create_user'), data={
            'username': 'testuser2',
            'password': 'complex_password',
            'last_name': 'user',
            'email': 'test@user.com'
        })
        self.assertEqual(response.status_code, 400)

    def test_login_success(self):
        response = self.client.post(reverse('login'), data={
            'username': self.USERNAME,
            'password': self.PASSWORD,
        })
        self.assertEqual(response.status_code, 200)

    def test_login_fail(self):
        response = self.client.post(reverse('login'), data={
            'username': 'wronguser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 401)
