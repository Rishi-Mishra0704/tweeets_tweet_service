from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tweet, Like, Comment
from .serializers import TweetSerializer

@api_view(['GET'])
def tweets_api(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return Response({'tweets': serializer.data})
