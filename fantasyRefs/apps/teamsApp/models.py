# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#import scrapy

# class refNames(scrapy.Spider):
# 	name = "Name"

# 	start_urls = ['http://operations.nfl.com/the-officials/these-officials-are-really-good/2017-roster-of-nfl-officials/']

# 	def parse(self, response):
# 		for href in 
# Create your models here.

# class Ref(models.Model):
# 	first_name = models.CharField(max_length=255)
# 	last_name = models.CharField(max_length=255)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)
class Ref(models.Model):
	number = models.IntegerField(default=0)
	name = models.CharField(max_length=255)
	position = models.CharField(max_length=255)
	years_experience = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)

	# def __str__(self):
	# 	return str(self.id) + ', ' + self.name
	
