from __future__ import unicode_literals
from django.db import models
import re , bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NO_NUMBERS = re.compile(r'[a-zA-Z]')


class UserManager(models.Manager): 
	def validateReg(self, request):

		errorList = [] #appending to this list
		if len(request.POST['first_name']) < 2 or len(request.POST['last_name']) < 2:
			errorList.append("The length of your first or last name needs to be more than 2 characters!") 
		if not EMAIL_REGEX.match(request.POST['email']):
			errorList.append("Your email needs to be valid") 
		if len(request.POST['password']) < 8 or request.POST['password'] != request.POST['confirmpassword']: 
			errorList.append("Passwords need to match!")   
		if not NO_NUMBERS.match(request.POST['first_name']):
			errorList.append("No numbers in your name")  
		if not  NO_NUMBERS.match(request.POST['last_name']):
			errorList.append("No numbers in your last name") 

		if len(errorList) > 0:
			return (False, errorList)
	
		pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		user = self.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], pw_hash=pw_hash)
		return (True, user)

	def validateLogin(self, request):

		user = self.filter(email=request.POST['email']) #filter gives you a list of the object (NOT THE EMAIL)!
		if len(user) == 0:
			return (False, ['Email does not match our records'])
		password = request.POST['password'].encode()
		if bcrypt.hashpw(password, user[0].pw_hash.encode()): 
			return (True, user[0])	

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	pw_hash = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	userManager = UserManager()
	objects = models.Manager()

class Appointment(models.Model):
	task_name = models.CharField(max_length=100, blank=True, null=True)
	task_date = models.CharField(max_length=100)
	task_time = models.CharField(max_length=100)
	
	userManager = UserManager()
	objects = models.Manager()