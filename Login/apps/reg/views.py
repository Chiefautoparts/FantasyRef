# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request, "reg/index.html")

def Register(request):
	status = User.objects.RegisterUser(request.POST)
	if len(status):
		for error in status:
			messages.error(request, error)
			return redirect("/")
	else:
		User = User.objects.get(id = id)
		User.Username = request.POST['Username']
		User.Email = request.POST['Email']
		user.save()
		messages.success("User has been Registered please Login")
		print user.password
		return redirect("/")
