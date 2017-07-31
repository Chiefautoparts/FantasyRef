# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from datetime import datetime
from django.db import models, IntegrityError

class UserManager(models.Manager):
    def registerValidation(self, postData):
        status = {'valid': True, 'errors': [], 'user': None}
        if not postData['name'] or len(postData['name']) <  3:
            status['valid'] = False
            status['errors'].append('FAKE NAME!!!!')
        if not postData['username'] or len(postData['username']) < 3:
            status['valid'] = False
            status['errors'].append('Username isnt good enough to be on this site. Pick a new one or leave')
        if not postData['email'] or not re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', postData['email']):
             status['valid'] = False
             status['errors'].append('INVALID EMAIL!!!!')
        if not postData['password'] or len(postData['password']) < 6:
            status['valid'] = False
            status['errors'].append('Password is too weak. TOO WEAK!!!!!')
        if postData['confirm_password'] != postData['password']:
            status['valid'] = False
            status['errors'].append('Your Passwords Don\'t match Dumbass.')
        
        user = User.objects.filter(email=postData['email'])

        if status['valid']:
            try:
               user = User.objects.create(
                    name=postData['name'],
                    username=postData['username'],
                    email=postData['email'],
                    password=(bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
                    )
               user.save()
               status['user'] = user
            except IntegrityError as e:
                status['valid']=False
                if 'UNIQUE constraint' in e.message:
                    status['errors'].append('email already registered in system')
                else: 
                    status['errors'].append(e.message)
        return status



    def loginValidation(self, postData):
        status = {'valid':True, 'errors': [], 'user':None}
        try:
            user = User.objects.get(email=postData['email'])
            if user.password == bcrypt.hashpw(postData['password'].encode(), user.password.encode()):
                pass
            else:
                raise Exception()
        except Exception as e:
            status['valid']=False
            status['errors'].append('Username or Password is incorrect')

        if status['valid']:
            status['user'] = user
        return status
        

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()













