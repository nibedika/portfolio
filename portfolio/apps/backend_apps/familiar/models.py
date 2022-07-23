from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension

from apps.access_apps.backend_access.models import User as backendUser


# Create your models here.
class Cl(models.Model):

	# General Info Fields
	date              = models.DateTimeField(auto_now_add=True)
	user_id           = models.ForeignKey(backendUser, on_delete=models.CASCADE, related_name='familiar_user_id')
	familiar_id       = models.CharField(max_length=50, blank=False)
	name              = models.CharField(max_length=255, blank=False)
	contact_no        = models.CharField(max_length=255, blank=False)
	address           = models.TextField(blank=True)
	contact_person    = models.CharField(max_length=255, blank=False)
	contact_person_no = models.CharField(max_length=255, blank=False)
	description       = models.TextField(blank=True)
	remark            = models.TextField(blank=True)
	photo             = models.FileField(max_length=100, blank=True)
	
	status            = models.CharField(default='active', max_length=50, blank=False) # active, inactive
	
	# Backup Fields
	trash             = models.BooleanField(default=False)

	def __str__(self):
		return self.familiar_id