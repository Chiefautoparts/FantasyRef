# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, IntegrityError
import bcrypt
import re

# Create your models here.
class UserManager(models.Manager):
    def registerValidation(self, postData):
        status = {'valid': True, 'errors': [], 'user': None}
        if not postData['name'] or len(postData['name']) < 3:
            status['valid'] = False
            status['errors'].append('You\'re never going to statisfy anybody with a name that short')
        if not postData['username'] or len(postData['username']) < 3:
            status['valid'] = False
            status['errors'].append('that is a stupid username try again')
        if not postData['email'] or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", postData['emial']):
            status['valid'] = False
            status['errors'].append('That email is less credible than CNN reporting')
        if not postData['password'] or len(postData['password']) < 6:
            status['valid'] = False
            status['errors'].append('Nope')
        if postData['confirm_password'] != postData['password']:
            status['valid'] = False
            status['errors'].append('Passwords do not match')
        if status['valid'] == False:
            return status

        user = User.objects.filter(email=postData['email'])

        if status['valid']:
            user = User.objects.create(name=postData['name'], username=postData['username'], email=postData['email'], password=(bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())))
            status['user'] = user
            return status		

		
    def loginValidation(self, postData):
        status = {'valid': True, 'errors':[], 'user': None}
        if status['user']:
            if user.password != bcrypt.hashpw(postData['password'].encode(), user.password.encode()):
                status['valid'] = False
                status['errors'].append('information is invalid. Again!!!!!')
            else:
                status['user'] = user.index
        else:
            status['valid'] = False
        return status

		# status={'valid':True, 'errors': [], 'user':None}
  #       user = User.objects.get(email=postData['email'])
  #       if user.password == bcrypt.hashpw(postData['password'].encode(), user.password.encode()):
  #           pass
  #       else:
  #           raise Exception()
  #       Exception e:
  #           status['valid']=False
  #           status['errors'].append('Username or Password is incorrect')

  #       if status['valid']:
  #           status['user'] = user
  #       return status

  


class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()