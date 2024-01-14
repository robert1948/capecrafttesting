from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("vision/", views.vision, name="vision"),
    path("note/", views.note, name="note"),
    path("all_addresses/", views.all_addresses, name="all_addresses"),
]
