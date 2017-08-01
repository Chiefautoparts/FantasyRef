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
		request.session['id'] = status['user'].id
		return redirect('login:success')
	return redirect('login:index')


def register(request):
	status = User.objects.registerValidation(request.POST)
	if not status['valid']:
		for error in status['errors']:
			messages.error(request, error)
	else:
		messages.success(request, 'User has been registered, now log in')
	return redirect('login:index')


def login(request):
	results = User.objects.loginVal(request.POST)
	if not results['status']:
		for error in results['errors']:
			messages.error(request, error)
	else:
		request.session['id'] = results['user'].id
		return redirect('login:success')
	return redirect('login:index')

def success(request):
	print "***"*250
	return redirect('refs:home')


# def show(request):
# 	user = User.objects.get(id=request.session['id'])
# 	context = {
	# 	'user': user
	# }
	# return render(request, 'refApp/TeamPages.html', context)