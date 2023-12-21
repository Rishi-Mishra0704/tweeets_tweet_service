from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import UserRegistrationForm, UserLoginForm

class AuthenticationViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_view(self):
        url = reverse('register')
        data = {'username': 'testuser', 'password1': 'testpassword123', 'password2': 'testpassword123'}
        
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200) 
        self.assertFalse(User.objects.filter(username='testuser').exists())

    def test_user_login_view(self):
        # Create a user for testing login
        user = User.objects.create_user(username='testuser', password='testpassword123')

        url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpassword123'}
        
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful login
        self.assertTrue(response.url, '/')

    def test_user_logout_view(self):
        # Login a user for testing logout
        user = User.objects.create_user(username='testuser', password='testpassword123')
        self.client.login(username='testuser', password='testpassword123')

        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after logout
        self.assertFalse(self.client.session.get('_auth_user_id'))  # Expecting no user in session after logout
