from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    url = models.URLField()
    category = models.CharField(max_length=64, default='uncategorised')
    active = models.BooleanField(default=True)

class Bid(models.Model):
    item = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='bids')
    price = models.FloatField()
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)


class Comments(models.Model):
    item = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    title = models.CharField(max_length=64)
