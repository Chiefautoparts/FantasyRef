# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt


from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def RegisterUser(self, postData):
		status = []
		if not postData['name'] or len(postData['name'])<3:
			status.append('Name must me more than 3 characters')
		if not postData['username'] or len(postData['username'])<3:
			status.append('Username must be more than 3 characters')
		if not postData['email'] or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", postData['email']): 	
			status.append('Invalid Email')
		if not postData['password'] or not len(postData['password'])<8:
			status.append('Your password is shit.')
		if postData['confirmPassword'] != postData['password']:
			status.append('Posswords do not match')

		if len(status) == 0:
			PW = (bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
			user = User.objects.create(name=postData['name'], username=postData['username'], email=postData['email'], password=PW)
			user.save()

		else:
			return status

	def LoginUser(self, postData):
		status = []
		if len(status) == 0:
			if user.password != bcrypt.hashpw(postData['password'].encode(), user.password.encode()):
				status.append("Login Information not valid. Try agian dip shit")
		else:
			return status



class User (models.Model):
	name = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()