from django import forms
from .models import Room


class RoomForm(forms.ModelForm):
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
