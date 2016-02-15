# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logic_world', '0003_auto_20160213_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorldElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField(blank=True, default=0, null=True)),
                ('y', models.IntegerField(blank=True, default=0, null=True)),
                ('z', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gate',
            fields=[
                ('worldelement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='logic_world.WorldElement')),
                ('output', models.BooleanField(default=False)),
                ('gate_type', models.CharField(max_length=200)),
            ],
            bases=('logic_world.worldelement',),
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('worldelement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='logic_world.WorldElement')),
                ('value', models.BooleanField(default=False)),
            ],
            bases=('logic_world.worldelement',),
        ),
        migrations.AddField(
            model_name='worldelement',
            name='creator_world_relation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='logic_world.UserWorldRelation'),
        ),
        migrations.AddField(
            model_name='input',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='input_left', to='logic_world.WorldElement'),
        ),
        migrations.AddField(
            model_name='gate',
            name='left_child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gate_left_input', to='logic_world.WorldElement'),
        ),
        migrations.AddField(
            model_name='gate',
            name='right_child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gate_right_input', to='logic_world.WorldElement'),
        ),
    ]