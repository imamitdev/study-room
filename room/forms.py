from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["name", "username", "email", "password1", "password2"]


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = [
            "topic",
            "name",
            "description",
        ]

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        # You can customize the form fields or add additional validation here if needed.


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["avatar", "name", "username", "email", "bio"]
