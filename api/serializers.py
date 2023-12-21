from rest_framework import serializers
from .models import Tweet, Like, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user__username', 'content']

class TweetSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Tweet
        fields = ['id', 'title', 'content', 'user__username', 'likes_count', 'comments']

    def get_likes_count(self, obj):
        return Like.objects.filter(tweet=obj).count()