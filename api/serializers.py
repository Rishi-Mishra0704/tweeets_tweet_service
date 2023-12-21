from rest_framework import serializers
from models import Tweet, Like, Comment


class TweetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tweet
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Comment
            fields = '__all__'