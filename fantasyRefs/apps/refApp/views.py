# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
	return render(request, 'refApp/index.html')

def loginUser(request):
	print '**LOGIN**'*50
	status = User.objects.loginValidation(request.POST)
	if status['valid'] != True:
		for error in status['errors']:
			messages.error(request, error)
		return redirect('login:index')
	else:
		request.session['id'] = status['user'].id
		return redirect('login:success')
	return redirect('login:index')


def register(request):
	print '**REGISTER**'*50
	status = User.objects.registerValidation(request.POST)
	if not status['valid']:
		for error in status['errors']:
			messages.error(request, error)
	else:
		messages.success(request, 'User has been registered, now log in')
	return redirect('login:index')



def success(request):
	print "**SUCCESS**" * 50
	return redirect('refs:home')


# def show(request):
# 	user = User.objects.get(id=request.session['id'])
# 	context = {
	# 	'user': user
	# }
	# return render(request, 'refApp/TeamPages.html', context)