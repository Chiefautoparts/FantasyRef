# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Ref
from . import ref_maker
# Create your views here.
def home(request):
	print '***************************TEAMS************************'
	return render(request, 'teamsApp/team/html')
	# return render(request, 'teamsApp/team.html')

def addTeam(request):
	available_refs = Ref.objects.all()
	context = {
		'refs': available_refs
	}

	return render(request, 'teamsApp/team.html', context)
	print '*'*100 + 'ADD TEAM' + '*'*100