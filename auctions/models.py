from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class Auction(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="watching")

    def __str__(self):
        return f"{self.id}: Auction {self.title} from {self.user}"

class Bid(models.Model):
    item = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='bids')
    price = models.FloatField()
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"${self.price} bid from {self.bidder}"

class Comment(models.Model):
    item = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: comment for Auction {self.item} from {self.user}"
