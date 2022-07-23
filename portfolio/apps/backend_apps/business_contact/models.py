from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator

from apps.access_apps.backend_access.models import User as backendUser


# Create your models here.
class Cl(models.Model):

	# Basic Info Fields
	date       = models.DateTimeField(auto_now_add=True)
	user_id    = models.ForeignKey(backendUser, on_delete=models.CASCADE, related_name='contact_user_id', blank=True)
	contact_id = models.CharField(max_length=250)       
	
	# Message Fields
	name       = models.CharField(max_length=150, blank=False) 
	email      = models.EmailField(validators=[EmailValidator], max_length=100, blank=False)
	subject    = models.CharField(max_length=150, blank=False) 
	text       = models.TextField(blank=True)
	file       = models.FileField(max_length=100, blank=True)
	
	# Message Status Info Fields
	status     = models.CharField(validators=[RegexValidator], max_length=50, default='unseen') #option-> seen, unseen
	
	# Backup Fields
	trash      = models.BooleanField(default=False)
	
	def __str__(self):
		return self.contact_id