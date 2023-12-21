from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.user.username}"


class Like(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} likes {self.tweet.title}"

class Comment(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Comment by {self.user.username} on {self.tweet.title}"
    

# models.py in your Django app

from django.db import models

class Follow(models.Model):
    follower = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='following', db_column='follower_id')
    followee = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='followers', db_column='followee_id')

    class Meta:
        managed = False
        db_table = 'follows'

    def __str__(self):
        return f"{self.follower.username} follows {self.followee.username}"