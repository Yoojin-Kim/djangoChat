from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import User
from .forms import UserForm
import json

def index(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
    else:
        form = UserForm()
    return render(request, 'chat/index.html', {'form': form})

def room(request, room_name):
    n = User.objects.count()
    username = User.objects.all()[n-1].name
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'user_name_json' : mark_safe(json.dumps(username)),
    })