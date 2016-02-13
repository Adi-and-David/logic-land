from django.contrib import admin
from .models import User
from .models import World
from .models import UserWorldRelation

admin.site.register(User)
admin.site.register(World)
admin.site.register(UserWorldRelation)

# Register your models here.
