from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # render index.html on /
    path("", views.home, name="home"),
    path("create-room/", views.createRoom, name="create-room"),
    path("update-room/<str:pk>/", views.updateRoom, name="update-room"),
    path("delete-room/<str:pk>/", views.deleteRoom, name="delete-room"),
    path("room/<int:room_id>/", views.room, name="room"),
    path("delete-message/<str:pk>/", views.deleteMessage, name="delete-message"),
    path("topics/", views.topics, name="topics"),
]
