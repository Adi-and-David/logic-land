from django.contrib import admin
from .models import CustomUser
from .models import World
from .models import UserWorldRelation

admin.site.register(CustomUser)
admin.site.register(World)
admin.site.register(UserWorldRelation)

# Register your models here.
