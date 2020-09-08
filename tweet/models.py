from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser

# Create your models here.

class Tweet(models.Model):
    tweet = models.TextField(max_length=140)
    time_date = models.DateTimeField(default=timezone.now)
    twitter_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name="twitter_user")
