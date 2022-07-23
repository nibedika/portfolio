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
	date                = models.DateTimeField(auto_now_add=True)
	msg_id              = models.CharField(max_length=250)       
	
	# Message Info Fields
	sender              = models.ForeignKey(backendUser, on_delete=models.CASCADE, related_name='mgs_sender')
	receiver            = models.ForeignKey(backendUser, on_delete=models.CASCADE, related_name='mgs_receiver')

	# Message Fields
	text                = models.TextField(blank=True)
	file                = models.FileField(max_length=100, blank=True)

	# Message Timing Info Fields
	publish             = models.DateTimeField(auto_now_add=True)
	created             = models.DateTimeField(auto_now_add=True)
	updated             = models.DateTimeField(auto_now=True)
	
	# Message Status Info Fields
	status              = models.CharField(validators=[RegexValidator], max_length=50, default='unseen') #option-> seen, unseen
	
	# Backup Fields
	trash               = models.BooleanField(default=False)
	
	def __str__(self):
		return self.msg_id