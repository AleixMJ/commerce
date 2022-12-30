from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing", views.listing, name="listing"),
    path("auction/<int:id>", views.auction, name="auction"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("addwatch/<int:id>", views.addwatch, name="addwatch"),
    path("removewatch/<int:id>", views.removewatch, name="removewatch"),
    path("bidding/<int:id>", views.bidding, name="bidding"),
    path("addcomment/<int:id>", views.addcomment, name="addcomment")


]
