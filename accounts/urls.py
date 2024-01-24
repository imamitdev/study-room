from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # render index.html on /
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.register, name="register"),
    path("update-profile/", views.profile_edit, name="update-profile"),
    path("user-profile/<str:username>/", views.user_profile, name="user-profile"),
]
