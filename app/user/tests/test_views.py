from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

TOKEN_URL = reverse('user:token')


def create_user(**params):
    """ create and return a new user """
    return get_user_model().objects.create_user(**params)


class PublicUserApiTest(TestCase):
    """ Test the public features of the user API """

    def setUp(self):
        self.client = APIClient()

    def test_create_token_for_user(self):
        """ Test generate token for valid credentials """
        user_details = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'Name',
            'password': 'test-user-password123'
        }
        create_user(**user_details)
        payload = {
            'username': user_details['email'],
            'password': user_details['password'],
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_bad_credentails(self):
        """ Test return error if credenatials are invalid """
        create_user(email='test@example.com', password="goodpass")
        payload = {
            'username': 'test@example.com',
            'password': 'badpass'
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_blank_password(self):
        """ Test posting a blank password return an error """
        payload = {
            'username': 'test@example.com',
            'password': ''
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
