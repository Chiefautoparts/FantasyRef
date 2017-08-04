from __future__ import unicode_literals
from django.db import models, IntegrityError
import bcrypt
import re

class UserManager(models.Manager):
	def registerVal(self, postData):
		results = {'status':True, 'errors':[], 'user':None}
		if not postData['name'] or len(postData['name']) < 3:
			results['status']=False
			results['errors'].append('enter a valid name')
		if not postData['username'] or len(postData['username']) < 3:
			results['status']=False
			results['errors'].append('enter a valid Username')
		if not postData['email'] or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", postData['email']):
			results['status']=False
			results['errors'].append('please enter a valid email')
		if not postData['password'] or len(postData['password']) < 6:
			results['status']=False
			results['errors'].append('please enter a valid password')
		if postData['password'] != postData['passvalid']:
			results['status'] = False
			results['errors'].append('Passwords do not match')

		user = User.objects.filter(email=postData['email'])

		if results['status']:
			try:
				user = User.objects.create(name=postData['name'], username=postData['username'], email=postData['email'], password=(bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())))
				user.save()
				results['user']=user
			except IntegrityError as e:
				results['status']=False
				if 'UNIQUE constraint'in e.message:
					results['errors'].append('email already in system')
				else:
					results['errors'].append(e.message)
		return results

	def loginVal(self, postData):
		results = {'status':True, 'errors':[], 'user':None}
		try:
			user = User.objects.get(email=postData['email'])
			if user.password == bcrypt.hashpw(postData['password'].encode(), user.password.encode()):
				pass
			else:
				raise Exception()
		except Exception as e:
			results['status']=False
			results['errors'].append('incorrect Username or password')

		if results['status']:
			results['user'] = user
		return results

class User(models.Model):
	name = models.CharField(max_length=255)
	username= models.CharField(max_length=255)
	email = models.CharField(max_length=255, unique=True)
	password = models.CharField(max_length=255)

	objects = UserManager()