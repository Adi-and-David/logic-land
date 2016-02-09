from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import World

def index(request):
    # Show all worlds
    worlds = World.objects.all()
    context = {
        'worlds': worlds
    }
    return render(request, "world/index.html", context)

def show(request, world_id):
    #Show world with id = id
    world = get_object_or_404(World, pk=world_id)
    return render(request, 'world/show.html', {'world': world})

#def create(request):
    #create a world
