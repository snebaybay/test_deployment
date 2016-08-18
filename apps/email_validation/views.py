from django.shortcuts import render, HttpResponse, redirect
from .models import Email
from datetime import datetime
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
	emails = Email.objects.all()
	context = { 
	'emails' :emails
	}
	return render(request, "email_validation/index.html", context)

def success(request): 

	if EMAIL_REGEX.match(request.POST['email_id']): 
		Email.objects.create(email_address = request.POST['email_id'], date_added= datetime.now(), updated_at= datetime.now())
		context = {'email_add' : request.POST['email_id'],
					'emails' :emails}
		return render(request, "email_validation/success.html", context)
	
	elif not EMAIL_REGEX.match(email_check):
		return HttpResponse('You must enter a valid email!')

	else:
		request.session.clear()



 
