from __future__ import unicode_literals

from django.db import models

# Create your models here.

class World(models.Model):
	user_count = models.IntegerField()

''' Test by commenting out
	Will be removed after testing.
class User(modelsdModel):
	email = models.CharField(max_length=200)
	user_name = models.CharField(max_length=200)
	world = models.ForeignKey(dWorld)
'''
class UserWorldRelation(models.Model):
	world =  models.ForeignKey(World)
	relationship_type = models.CharField(max_length=200)
