# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import random

def index(request):
	User.objects.create_user(first_name="Ricky", last_name="Bobby", username=str(random.randint(0-100)))
	users = User.objects.all()
	return render(request, 'TestUser/User.html', {'users': users})

# Create your views here.
def login()