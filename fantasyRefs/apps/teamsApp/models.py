# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..refApp.models import User
from django.db import models


class League(models.Model):
	name = models.CharField(max_length=255)
	subDivision = models.CharField(max_length=255)
	created_at =  models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Ref(models.Model):
	number = models.IntegerField(default=0)
	name = models.CharField(max_length=255)
	league = models.ForeignKey(League, related_name='league')
	division = models.ForeignKey(League, related_name='division')
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)

''' Future addins
class UserTeam(models.Model):
	currRefs = models.ManyToManyField(Ref, related_name='currRefs')
	currLeague = models.ForeignKey(UserLeague, related_name='currLeague')
	teamName = models.CharField(max_length=100)
	created_at =  models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class UserLeague(models.Model):
	leagueName = models.ChrarField(max_length=50)
	#sports = models.ForeignKey(Sport, related_name='sports0') eventually will make multiple sports available'''