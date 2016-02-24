from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User as DjangoUser

# Create your models here.

# User table and World table should have many-to-many relationship.
class CustomUser(DjangoUser):
  auth_user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE, default='')
  world_count = models.IntegerField(default=0, blank=True, null=True)

class World(models.Model):
  world_name = models.CharField(max_length=200, default='Untitled')
  creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
  user_count = models.IntegerField(default=0, blank=True, null=True)

  @classmethod
  def create(cls, world_name):
    if world_name is None:
      world = cls(world_name=world_name)
      world.save()
    else:
      world = cls()
      world.save()
    return world

class UserWorldRelation(models.Model):
  world = models.ForeignKey(World, on_delete=models.CASCADE, null=True)
  custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
  relationship_type = models.CharField(max_length=200)

class WorldElement(models.Model):
  creator_world_relation = models.ForeignKey(UserWorldRelation, on_delete=models.CASCADE, null=True)
  x = models.IntegerField(default=0, blank=True, null=True)
  y = models.IntegerField(default=0, blank=True, null=True)
  z = models.IntegerField(default=0, blank=True, null=True)
  value = models.BooleanField(default=False)

  def get_position():
    return x, y, z

class Input(WorldElement):
  parent = models.ForeignKey(WorldElement, on_delete=models.CASCADE, null=True, related_name='input_left')


class Gate(WorldElement):
  left_child = models.ForeignKey(WorldElement, on_delete=models.CASCADE, null=True, related_name='gate_left_input')
  right_child = models.ForeignKey(WorldElement, on_delete=models.CASCADE, null=True,  related_name='gate_right_input')
  gate_type = models.CharField(max_length=200)

  def compute_value():
    if gate_type == 'AND':
      self.value = (right_child.value & left_child.value)
    elif gate_type == 'OR':
      self.value = (right_child.value | left_child.value)
    elif gate_type == 'NOT':
      self.value = not(left_child.value)
    # TO DO
    # elif gate_type == 'XOR':
    # elif gate_type == 'NOR':
    # elif gate_type == 'NAND':


