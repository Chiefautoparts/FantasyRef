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
        if status['valid'] is False:
            return status 
        
        user = User.objects.filter(username=postData['username'])

        if user:
            status['valid'] = False
            status['errors'].append('you dun Fucked Up. Come on it doesn\'t take rocket appliances do do this')

        if status['valid']:
               user = User.objects.create(
                    name=postData['name'],
                    username=postData['username'],
                    email=postData['email'],
                    password=(bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
                    )
               user.save()
               status['user'] = user
        return status

    def loginValidation(self, postData):
        status = {'valid':True, 'errors': [], 'user':None}
        user = User.objects.filter(username=postData['username'])
        try:
            user[0]
        except IndexError:
            status['valid'] = False
            status['errors'].append('No account is found so you are wrong. DO IT AGAIN!!')

        if user[0]:
            if user[0].password !=bcrypt.hashpw(postData['password'].encode(), user[0].password.encode()):
                status['status'] = False
                status['errors'].append('WRONG!!!')
            else:
                status['user'] = user[0].id   
        else:
            status['status'] = False
        return logged

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + ', ' + self.username

    objects = UserManager()













