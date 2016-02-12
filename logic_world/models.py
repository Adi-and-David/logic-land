from __future__ import unicode_literals

from django.db import models

# Create your models here.

class World(models.Model):
	user_count = models.IntegerField()

class UserWorldRelation(models.Model):
	world =  models.ForeignKey(World)
	relationship_type = models.CharField(max_length=200)
