from django.shortcuts import render
from django.template import loader

from .models import World

def index(request):
    # Show all worlds
    worlds = World.objects.all()
    context = {
        'worlds': worlds
    }
    return render(request, "world/index.html", context)

#def show(request, world_id):
    #Show world with id = id

#def create(request):
    #create a world
