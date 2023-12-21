from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Tweet, Comment

class TweetAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.tweet = Tweet.objects.create(title='Test Tweet', content='This is a test tweet', user=self.user)

    def test_create_tweet(self):
        url = reverse('create_tweet_api')
        data = {'title': 'New Tweet', 'content': 'This is a new tweet'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tweet.objects.count(), 2) 
        self.assertEqual(Tweet.objects.last().title, 'New Tweet')


    def test_get_tweets(self):
        url = reverse('tweets_api')

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('tweets', response.data)
        self.assertEqual(len(response.data['tweets']), Tweet.objects.count())

    def test_comment_tweet(self):
        url = reverse('comment_tweet', args=[self.tweet.id])
        data = {'content': 'This is a comment on the tweet.'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.get().content, 'This is a comment on the tweet.')

    def test_comment_tweet_not_found(self):
        url = reverse('comment_tweet', args=[999]) 
        data = {'content': 'This is a comment on a non-existent tweet.'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Comment.objects.count(), 0)
