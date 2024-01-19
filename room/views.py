from django.shortcuts import render, redirect
from .models import Room, Topic
from django.db.models import Q


# Create your views here.
def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)
    )
    topics = Topic.objects.all()[0:5]
    context = {"rooms": rooms, "topics": topics}
    return render(request, "home.html", context)
