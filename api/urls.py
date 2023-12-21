from django.urls import path
from . import views
urlpatterns = [
path('tweets/', views.tweets_api, name='tweets_api'),
]