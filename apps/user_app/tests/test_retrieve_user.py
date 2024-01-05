from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import User
from django.urls import reverse


class RetrieveUserDataViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345',
                                             first_name='test', last_name='user', email='test@login.com')
        self.url = reverse('retrieve_user', kwargs={'pk': self.user.pk})

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_serializer_usage(self):
        response = self.client.get(self.url)
        self.assertIn('username', response.data)

    def test_user_data_retrieval(self):
        token = self.get_tokens_for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)
        self.assertEqual(response.data['first_name'], self.user.first_name)
        self.assertEqual(response.data['last_name'], self.user.last_name)
        self.assertEqual(response.data['email'], self.user.email)
