from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'head': 'tail'})


def roomname(request, room_name):
    return render(request, 'room.html', {"room_name": room_name})