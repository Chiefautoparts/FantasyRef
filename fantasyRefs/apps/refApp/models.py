# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from datetime import datetime
from django.db import models

class UserManager(models.Manager):
    def registerValidation(self, postData):
        status = {'valid': True, 'errors': [], 'user': None}
        if not postData['name'] or len(postData['name']) <  3:
            status['valid'] = False
            status['errors'].append('FAKE NAME!!!!')
        if not postData['username'] or len(postData['username']) < 3:
            status['valid'] = False
            status['errors'].append('Username isnt good enough to be on this site. Pick a new one or leave')
        # if not re.postData['email'](r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$)'):
        #     status['valid'] = False
        #     status['errors'].append('INVALID EMAIL!!!!')
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
            status['valid'] =False
            status['errors'].append('Failed at life... I mean failed to register user')

        if status['valid']:
            userpassword = bcrypt.hashpw(postData['password'].encode, bcrypt.gensalt())
            user = User.objects.create(
                name = postData['name'],
                username = postData['username'],
                email = postData['email'],
                password = userpassword
                )
            status['user'] = user
        return status

    def loginValidation(self, postData):
        status = {'valid':True, 'errors': [], 'user':None}
        user = User.objects.filter(username=postData['username'])
        try:
            user[0]
        except IndexError:
            status['valid'] = False
            status['errors'].append('This infor provided is about as credible as CNN. try again')

        if user[0]:
            if user[0].password != bcrypt.hashpw(postData['userpassword'].encode(), user[0].password.encode()):
                status['valid'] = False
                status['errors'].append('el passwordo is no goodo')
            else:
                status['user']=user[0].id
        else:
            status['valid'] = False
        return status


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













