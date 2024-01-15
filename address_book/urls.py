from django.urls import path
from . import views

urlpatterns = [
path("add_address", views.add_address, name="add_address"), 
path("my_address_book", views.my_address_book, name="my_address_book"),
path("my_view", views.my_view, name="my_view"),
path("address_list", views.address_list, name="address_list"),
path("addreses", views.addresses, name="addresses")
]
