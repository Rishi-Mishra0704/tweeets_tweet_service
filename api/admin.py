from django.contrib import admin
from .models import Tweet, Like, Comment, Follow
# Register your models here.
admin.site.register(Tweet)
admin.site.register(Like)
admin.site.register(Follow)
admin.site.register(Comment)