from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Tweet, Like, Comment
from .serializers import TweetSerializer
@api_view(['GET'])
def tweets_api(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return Response({'tweets': serializer.data})


@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_tweet_api(request):
    serializer = TweetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response({'status': 'Tweet created'}, status=201)
    return Response(serializer.errors, status=400)