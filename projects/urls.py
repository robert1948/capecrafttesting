from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("website.urls")),
    path("members/", include("members.urls")),
    path("members/", include("django.contrib.auth.urls")),
    path("blog/", include("blog.urls")), # new
    path("address_book/", include("address_book.urls")) # new
    
]
