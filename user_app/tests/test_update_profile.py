import tempfile
from PIL import Image

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.urls import reverse

from user_app.models import UserProfileModel


class UpdateProfileViewTestsWithJWT(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='asdasd123',
            first_name='test', last_name='user', email='test@user.com')
        self.profile = UserProfileModel.objects.get(
            owner=self.user)
        self.url = reverse('update-profile', kwargs={'pk': self.profile.pk})

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def create_test_file(self):
        image = Image.new('RGB', (100, 100), color='red')
        temp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(temp_file, format='JPEG')
        temp_file.seek(0)
        return temp_file

    def test_file_upload(self):
        token = self.get_tokens_for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        with self.create_test_file() as test_file:
            data = {'profile_picture': test_file}
            response = self.client.put(self.url, data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.profile.refresh_from_db()
        self.assertTrue(self.profile.profile_picture)
