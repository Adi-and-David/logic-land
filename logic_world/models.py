from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User as DjangoUser

# Create your models here.

# User table and World table should have many-to-many relationship.
class CustomUser(DjangoUser):
  auth_user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE, default='')
  world_count = models.IntegerField(default=0, blank=True, null=True)

class World(models.Model):
  creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
  user_count = models.IntegerField(default=0, blank=True, null=True)

class UserWorldRelation(models.Model):
  world = models.ForeignKey(World, on_delete=models.CASCADE, null=True)
  custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
  relationship_type = models.CharField(max_length=200)

class WorldElement(models.Model):
  creator_world_relation = models.ForeignKey(UserWorldRelation, on_delete=models.CASCADE, null=True)
  x = models.IntegerField(default=0, blank=True, null=True)
  y = models.IntegerField(default=0, blank=True, null=True)
  z = models.IntegerField(default=0, blank=True, null=True)

