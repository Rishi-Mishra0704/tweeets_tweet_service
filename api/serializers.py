from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tweet, Like, Comment
class CommentSerializer(serializers.ModelSerializer):
    user__username = serializers.ReadOnlyField(source='user.username')  # Adjust this line

    class Meta:
        model = Comment
        fields = [ 'user__username', 'content']

class TweetSerializer(serializers.ModelSerializer):
    user__username = serializers.ReadOnlyField(source='user.username')
    likes_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'title', 'content', 'user__username', 'likes_count', 'comments']

    def get_likes_count(self, obj):
        return Like.objects.filter(tweet=obj).count()