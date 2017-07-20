# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
	return render(request, 'refApp/index.html')

def loginUser(request):
	status = User.objects.loginValidation(request.POST)
	if not status['valid']:
		for error in status['errors']:
			messages.error(request, error)
	else:
		request.session['id']= status['user'].id
		return redirect('/show')
	return redirect('/')

def register(request):
	status = User.objects.registerValidation(request.POST)
	if not status['valid']:
		for error in status['errors']:
			messages.error(request, error)
	else:
		request.session['id'] = status['user'].id
		return redirect('/show')
	return redirect('/')

def show(request):
	user = User.objects.get(id=request.session['id'])
	context = {
		'user': user
	}
	return render(request, 'refApp/TeamPages.html', context)