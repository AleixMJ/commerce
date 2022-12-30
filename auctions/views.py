from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Auction, Bid, Comment, Category, Watchlist


def index(request):
    return render(request, "auctions/index.html", {
        "auctions": Auction.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def listing(request):

    if request.method == "POST":
        title = request.POST["title"]
        image = request.POST["image"]
        text = request.POST["text"]
        category = Category.objects.get(title=request.POST["category"])
        price = float(request.POST["price"])
        user = request.user
        new_listing = Auction(title=title, url=image,text=text,category=category, user=user, price=price)
        new_listing.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        user = request.user
        return render(request, "auctions/listing.html", {
            "categories": Category.objects.all()
        })

def auction(request):
    auction = Auction.objects.get(id=request.POST["auction"])
    print(auction)
    if request.method == "POST":
        return render(request, "auctions/auction.html", {
            "auction": auction
        })

@login_required
def watchlist(request):
    user= request.user     
    if request.method == "POST":           
        auction = Auction.objects.get(id=request.POST["auction"])
        fav = Watchlist(item=auction, user=user)
        fav.save()
        return render(request, "auctions/auction.html", {
            "auction": auction
        })

    else:
        return render(request, "auctions/watchlist.html", {
        "auctions": Watchlist.objects.filter(user=user)
    })