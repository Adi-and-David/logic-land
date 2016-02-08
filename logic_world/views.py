from django.http import HttpResponse
from django.template import loader

from .models import World

def index(request):
    # Show all worlds
    worlds = World.objects.all()
    template = loader.get_template("world/index.html")
    context = {
        'worlds': worlds
    }
    return HttpResponse(template.render(context,request))

#def show(request, world_id):
    #Show world with id = id

#def create(request):
    #create a world
