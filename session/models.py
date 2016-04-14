
# 
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
	#TODO : enforce validators
	client = models.ForeignKey(User,on_delete = models.CASCADE)
	ip = models.CharField(max_length = 30)
	def __str__(self):
		return str(self.client.pk) + " : " + self.client.username + " ("+self.ip+")"

