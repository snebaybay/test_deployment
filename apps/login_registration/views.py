from django.shortcuts import render, HttpResponse, redirect
from .models import User, Appointment
from datetime import datetime
import re 
from django.contrib import messages  
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
	
	return render(request, "login_registration/index.html")

def login(request):
	if request.method == 'POST':
		result = User.userManager.validateLogin(request)

		if result[0] == False:
			print('User/Login does not match!') #you can also say result[1]
			print_messages(request, result[1])
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

		return redirect('/appointment')

def register(request):
	if request.method == 'POST':
		result = User.userManager.validateReg(request) #result is the user object 
		if result[0] == False:
			print ('You have an error')
			print_messages(request, result[1])
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
		return redirect('/appointment')

def print_messages(request, message_list):
	for message in message_list:
		messages.add_message(request, messages.INFO, message)


def success(request):

	appointment = Appointment.userManager.all()
	context = {'appointment' : appointment, 
				'time' : datetime.now().strftime('%m/%d/%Y'),
				'future_time' :datetime.now().strftime('%I:%M:%S %p'),
			 }
	
	return render(request, "login_registration/sucess.html", context)

def create(request):
	Appointment.userManager.create(task_name = request.POST['task_name'], task_date= request.POST['task_date'], task_time= request.POST['task_time'])
	print Appointment.userManager.all()
	return redirect('/appointment')

def delete(request, id): 
	Appointment.userManager.filter(id=id).delete()
	return redirect('/appointment')

def edit(request, id):
	appointment = Appointment.userManager.all()
	context = {'appointment' : appointment}
	return render(request, "login_registration/edit.html", context)


def logout(request):
	request.session.clear()
	return redirect('/')




