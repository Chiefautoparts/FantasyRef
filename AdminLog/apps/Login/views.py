# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

def index(request):
	form = RegisterForm()
	context = { "regForm": form }
	return render(request, "Login/index.html", context)
	print '**INDEX**'*300

def register(request):
	if request.method == "POST":
		bound_form = RegisterForm(request.POST)
		print bound_form.is_valid()
		print bound_form.errors

		return redirect('index')

def make_messages(request):
	errors = [
		"First Error",
		"Second Error",
		"Third Error",
	]
	for error in errors:
		messages.error(request, error)
	return redirect('show_errors')

def show_errors(request):
	return render(request, 'Login/show_errors.html')