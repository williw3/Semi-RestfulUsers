from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
	def basic_validator(self, postData):
		message = 'field should contain at least one character'
		errors = {}
		if len(postData['fname']) < 1:
			errors['first_name'] = message
		if len(postData['lname']) < 1:
			errors['last_name'] = message
		if len(postData['email']) < 1:
			errors['email'] = message
		return errors


class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	objects = UserManager()



