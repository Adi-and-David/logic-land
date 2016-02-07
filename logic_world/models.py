from __future__ import unicode_literals

from django.db import models

# Create your models here.

class World(models.Model):
	user_count = models.IntegerField()

class User(models.Model):
	email = models.CharField(max_length=200)
	user_name = models.CharField(max_length=200)
	world = models.ForeignKey(World)

class UserWorldRelation(models.Model):
	user = models.ForeignKey(User)
	world =  models.ForeignKey(World)
	relationship_type = models.CharField(max_length=200)
