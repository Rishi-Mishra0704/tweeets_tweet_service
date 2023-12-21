from django.urls import path
from . import views
urlpatterns = [
    path('tweets/', views.tweets_api, name='tweets_api'),
    path('tweets/create/', views.create_tweet_api, name='create_tweet_api'),
    path('tweets/<int:tweet_id>/comment/', views.comment_tweet, name='comment_tweet'),
]
