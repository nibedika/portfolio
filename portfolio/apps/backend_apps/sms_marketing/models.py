from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator

from apps.access_apps.backend_access.models import User as backendUser


class Contact_list(models.Model):

	# Basic Info Fields
	date    = models.DateTimeField(auto_now_add=True)
	list_id = models.CharField(max_length=50)       
	user_id = models.ForeignKey(backendUser, on_delete=models.CASCADE, related_name='sms_marketing_list_user')
	
	# Contact Fields
	contact = models.CharField(max_length=150) 
	name    = models.CharField(max_length=150) 
	remark  = models.TextField(blank=True)
	
	# Message Status Info Fields
	status  = models.CharField(validators=[RegexValidator], max_length=50, default='active') #option-> inactive, active
	
	# Backup Fields
	trash   = models.BooleanField(default=False)
	
	def __str__(self):
		return self.list_id



# Create your models here.
class Cl(models.Model):

	# Basic Info Fields
	date             = models.DateTimeField(auto_now_add=True)
	sms_id           = models.CharField(max_length=50)       
	user_id          = models.ForeignKey(backendUser, on_delete=models.CASCADE, related_name='sms_marketing_user')
	
	# SMS Fields
	sender_contact   = models.CharField(max_length=150) 
	receiver_contact = models.ForeignKey(Contact_list, on_delete=models.CASCADE, related_name='receiver_sms')
	text             = models.TextField(blank=True)
	
	# Message Status Info Fields
	status           = models.CharField(validators=[RegexValidator], max_length=50, default='unseen') #option-> seen, unseen
	
	# Backup Fields
	trash            = models.BooleanField(default=False)
	
	def __str__(self):
		return self.sms_id