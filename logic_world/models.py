from __future__ import unicode_literals

from django.db import models

# Create your models here.

class World(models.Model):
	user_count = models.IntegerField(default=0, blank=True, null=True)

# User table and World table should have many-to-many relationship.
class User(models.Model):
  world_count = models.IntegerField(default=0, blank=True, null=True)

class UserWorldRelation(models.Model):
	world =  models.ForeignKey(World)
	relationship_type = models.CharField(max_length=200)
