from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # render index.html on /
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
]
