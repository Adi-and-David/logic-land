from django.test import TestCase

from logic_world.models import World

class WorldTestCase(TestCase):
    def setUp(self):
        self.assertEqual(World.objects.all().count, 0)
        World.objects.create()
        self.assertEqual(World.objects.all().count, 1)
