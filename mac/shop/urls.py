from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="search"),
    path("contact/", views.contact, name="ContactUs"),
    path("productview/", views.productview, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
]