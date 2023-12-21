from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Tweet

class TweetAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_tweet(self):
        url = '/api/tweets/'
        data = {'title': 'New Tweet', 'content': 'This is a new tweet'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tweet.objects.count(), 1)
        self.assertEqual(Tweet.objects.get().title, 'New Tweet')

    def test_create_tweet_unauthenticated(self):
        url = '/api/tweets/'
        data = {'title': 'New Tweet', 'content': 'This is a new tweet'}

        # Note: This test assumes you don't allow unauthenticated users to create tweets
        client = APIClient()
        response = client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Tweet.objects.count(), 0)