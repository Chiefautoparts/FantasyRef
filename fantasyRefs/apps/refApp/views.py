# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import User
# Create your views here.
def index(request):
	return render(request, 'refApp/index.html')

def loginUser(request):
	status = User.objects.loginValidation(request.POST)
	if not status['valid']:
		for error in status['errors']:
			messages.error(request, error)
		return redirect('/')
	else:
		user = User.objects.filter(id=results['id'])
		request.session['id']= user.id
	return redirect('Team:home')
	print 'login success' + '*'*100

def register(request):
	status = User.objects.registerValidation(request.POST)
	if not status['valid']:
		for error in status['errors']:
			messages.error(request, error)
		return redirect('/')
	request.session['id'] = status['user'].id
	return redirect('Team:home')
	print 'Register'*500


