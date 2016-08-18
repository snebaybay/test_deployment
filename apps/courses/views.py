from django.shortcuts import render, HttpResponse, redirect
from .models import Courses 
from datetime import datetime

def index(request):
	
	courses = Courses.objects.all()
	context = { 
	'courses' :courses
	}
	return render(request, "courses/index.html", context)

def create(request):  
	Courses.objects.create(course_name = request.POST['course_id'], description= request.POST['course_description'], date_added= datetime.now())
	return redirect('/')

def delete(request, id): #grabbing the specific id of the course you want to delete
	course_to_delete = Courses.objects.get(id=id)
	return render(request, "courses/show.html", { 'course' : course_to_delete })
 
def destroy(request,id): #deleting the specific id of the course you want to delete
	Courses.objects.filter(id=id).delete()
	return redirect('/')








