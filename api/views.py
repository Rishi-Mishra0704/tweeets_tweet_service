from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Tweet, Like, Comment
from .serializers import TweetSerializer, CommentSerializer, LikeSerializer
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

@api_view(['POST'])
def comment_tweet(request, tweet_id):
    try:
        tweet = Tweet.objects.get(pk=tweet_id)
    except Tweet.DoesNotExist:
        return Response({'detail': 'Tweet not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, tweet=tweet)
        return Response({'detail': 'Comment added successfully.'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)