from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import User
from room.models import Topic


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "login_register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect("home")
            else:
                messages.error(request, "Invalid login credentials")
    else:
        form = AuthenticationForm()
    return render(request, "login_register.html", {"form": form, "page": "login"})


@login_required(login_url="login")
def user_logout(request):
    auth.logout(request)
    messages.success(request, "You are Logged out")
    return redirect("login")


@login_required(login_url="login")
def profile_edit(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("home")
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, "profile-edit.html", {"form": form})


def user_profile(request, username):
    user = User.objects.get(username=username)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {
        "user": user,
        "rooms": rooms,
        "room_messages": room_messages,
        "topics": topics,
    }
    return render(request, "profile.html", context)
