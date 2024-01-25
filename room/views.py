from django.shortcuts import render, redirect, HttpResponse
from .models import Room, Topic, Message
from django.db.models import Q
from .forms import RoomForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)
    )
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))[0:3]
    topics = Topic.objects.all()[0:5]

    context = {
        "rooms": rooms,
        "topics": topics,
        "room_messages": room_messages,
    }
    return render(request, "home.html", context)


@login_required(login_url="login")
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


@login_required(login_url="login")
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)

    # Check if the current user is the host of the room
    if request.user != room.host:
        return HttpResponse("You are not allowed here!!")

    if request.method == "POST":
        # Update the Room instance with the new data
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            # Save the updated Room instance
            form.save()
            return redirect("home")
    else:
        # If it's a GET request, initialize the form with the existing room data
        form = RoomForm(instance=room)

    context = {"form": form, "room": room}
    return render(request, "room/create-room.html", context)


@login_required(login_url="login")
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse("You are not allowed here!!")

    if request.method == "POST":
        room.delete()
        return redirect("home")
    context = {"obj": room}

    return render(request, "room/delete.html", context)


def room(request, room_id):
    room = Room.objects.get(id=room_id)
    room_messages = room.message_set.all()
    participants = room.participants.all()

    if request.method == "POST":
        message = Message.objects.create(
            user=request.user, room=room, body=request.POST.get("body")
        )
        room.participants.add(request.user)
        return redirect("room", room_id=room.id)

    context = {
        "room": room,
        "room_messages": room_messages,
        "participants": participants,
    }
    return render(request, "room/room.html", context)


@login_required(login_url="login")
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse("You are not allowed here!!")

    if request.method == "POST":
        message.delete()
        return redirect("home")
    context = {"obj": message}
    return render(request, "room/delete.html", context)


def topics(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    topics = Topic.objects.filter(Q(name__icontains=q))
    context = {
        "topics": topics,
    }
    return render(request, "room/topics.html", context)
