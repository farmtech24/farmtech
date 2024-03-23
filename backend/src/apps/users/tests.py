# backend/apps/users/tests.py

from django.test import TestCase, Client
from django.urls import reverse
from .models import User

class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_user_registration(self):
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'farm_name': 'Test Farm',
        })
        self.assertEqual(response.status_code, 302)  # Check if registration was successful

        # Check if user is created in the database
        self.assertTrue(User.objects.filter(username='testuser').exists())

    # Add more test cases as needed for other scenarios

# You can also write tests for your login view, similar to the registration test case
