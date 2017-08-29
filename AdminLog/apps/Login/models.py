# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
def validateLengthGreaterThanTwo(value):
	if len(value) < 3:
		raise ValidationError(
			'{}must be longer than 2'.format(value)
			)
class User(models.Model):
	first_name = models.CharField(max_length=45, validators = [validateLengthGreaterThanTwo])
	last_name = models.CharField(max_length=45, validators = [validateLengthGreaterThanTwo])
	email = models.EmailField()
	password = models.CharField(max_length=100)
	confirm_password = models.CharField(max_length=100)