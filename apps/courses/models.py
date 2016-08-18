from __future__ import unicode_literals

from django.db import models

class Courses(models.Model):
	course_name= models.CharField(max_length=100, blank=True, null=True)
	description= models.CharField(max_length=100, blank=True, null=True)
	date_added= models.DateTimeField(blank=True, null=True)
	updated_at= models.DateTimeField(blank=True, null=True)
