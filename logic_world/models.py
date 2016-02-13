from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User as DjangoUser

# Create your models here.

class World(models.Model):
	user_count = models.IntegerField()

# User table and World table should have many-to-many relationship.
class User(DjangoUser):
  world_count = models.IntegerField(default=None, blank=True, null=True)

class UserWorldRelation(models.Model):
	world =  models.ForeignKey(World)
	relationship_type = models.CharField(max_length=200)
