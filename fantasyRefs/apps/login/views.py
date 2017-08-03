from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

def index(request):
	# if request.session.get('id'):
	# 	return redirect('katBook:userPage')

	return render(request, 'login/index.html')


def register(request):
	
	results = User.objects.registerVal(request.POST)
	

	if not results['status']:
		for error in results['errors']:
			messages.error(request, error)
			
	else:
		messages.success(request, 'User created, please log in.')
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

def logout(request):
	request.session.clear()
	return redirect('login:index')

def success(request):
	user = User.objects.get(id=request.session['id'])
	
	return redirect('refs:home')
