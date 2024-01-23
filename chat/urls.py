# mysite/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("pear/", include("pear.urls")),
    path("admin/", admin.site.urls),
]