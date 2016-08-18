from django.shortcuts import render, HttpResponse, redirect
from .models import User
from datetime import datetime
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
	
	return render(request, "login_registration/index.html")

def login(request):
	if request.method == 'POST':
		result = User.userManager.validateLogin(request)

		if result[0] == False:
			print('User/Login does not match!') #you can also say result[1]
			return redirect('/')

		print('*')*10	
		print('YAY YOU LOGGED IN!')
		
		user = result[1]
		request.session['user'] = { 
		'id' : user.id,
		'first_name' :user.first_name, 
		'last_name' :user.last_name,
		'email' :user.email,
		'method' :'logged in'
		}

		return redirect('/success')

def register(request):
	if request.method == 'POST':
		result = User.userManager.validateReg(request) #result is the user object 
		if result[0] == False:
			print ('You have an error')
			return redirect('/')
		
		print('*')*10
		print "YAY user registered!"
		user = result[1]
		request.session['user'] = { 
		'id' : user.id,
		'first_name' :user.first_name, 
		'last_name' :user.last_name,
		'email' :user.email,
		'method' :'Registered!'
		}
		return redirect('/success')


def success(request):
	return render(request, "login_registration/sucess.html")

def logout(request):
	request.session.clear()
	return redirect('/')
