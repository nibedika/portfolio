from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator

from apps.access_apps.backend_access.models import User as backendUser


# Create your models here.
class Cl(models.Model):

	# General Info Fields
	date           = models.DateTimeField(auto_now_add=True)
	resume_id      = models.CharField(max_length=50, blank=False)
	user_id        = models.ForeignKey(backendUser, on_delete=models.CASCADE, related_name='resume_user_id')
	
	resume_type    = models.CharField(validators=[RegexValidator], max_length=50, default='none') #option-> education, work
	duration       = models.CharField(max_length=150, blank=False)
	resume_title   = models.TextField(blank=True)
	resume_txt     = models.TextField(blank=True)
	institute      = models.CharField(max_length=200, blank=False)
	institute_logo = models.FileField(max_length=100, blank=True)
	url            = models.TextField(blank=True)
	
	status         = models.CharField(validators=[RegexValidator], max_length=180, default='inactive') #option-> active, inactive 
	
	# Backup Fields
	trash          = models.BooleanField(default=False)
	
	def __str__(self):
		return self.resume_id