from django.shortcuts import render, redirect
from .models import Room, Topic
from django.db.models import Q
from .forms import RoomForm


# Create your views here.
def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)
    )
    topics = Topic.objects.all()[0:5]
    context = {"rooms": rooms, "topics": topics}
    return render(request, "home.html", context)


def createRoom(request):
    if request.method == "POST":
        # Get the Topic instance based on the value from the request
        topic_id = request.POST.get("topic")
        topic_instance = Topic.objects.get(pk=topic_id)

        Room.objects.create(
            host=request.user,
            topic=topic_instance,
            name=request.POST.get("name"),
            description=request.POST.get("description"),
        )
        return redirect("home")
    else:
        form = RoomForm()
    return render(request, "room/create-room.html", {"form": form})
