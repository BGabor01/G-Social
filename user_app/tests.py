from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserAppTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='testloginuser', password='asdasd123',
                                 first_name='test', last_name='login', email='test@login.com')

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
            'username': 'testloginuser',
            'password': 'asdasd123',
        })
        self.assertEqual(response.status_code, 200)

    def test_login_fail(self):
        response = self.client.post(reverse('login'), data={
            'username': 'testloginuser2',
            'password': 'mjfhzeiw',
        })
        self.assertEqual(response.status_code, 401)
