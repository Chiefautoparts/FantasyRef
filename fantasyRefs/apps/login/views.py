# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, 'login/index.html')

def login(request):
	print '**LOGIN**'*100

def register(request):
	print '**REGISTER**'*100

def success(request):
   	return redirect('refs:home')
	print '**SUCCESS**'*100