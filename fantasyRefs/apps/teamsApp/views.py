# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Ref, League, User
from . import ref_maker
# Create your views here.

	
def home(request):
	content = {
		'refs': Ref.objects.all(),
		'leagues': League.objects.all(),
		'users': User.objects.get(id=request.session['id']),
	}
	return render(request, 'teamsApp/team/html', context)

def refMaker(request):
	ref_maker.random_ref(60)
	ref_maker.LeagueMaker(12)