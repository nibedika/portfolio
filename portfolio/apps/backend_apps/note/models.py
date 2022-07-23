from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension

from apps.access_apps.backend_access.models import User as backendUser


# Create your models here.
class Cl(models.Model):

	# General Info Fields
	date        = models.DateTimeField(auto_now_add=True)
	user_id     = models.ForeignKey(backendUser, on_delete=models.CASCADE, related_name='note_user_id')
	note_id     = models.CharField(max_length=50, blank=False)
	note_date   = models.DateTimeField(auto_now_add=True)
	title       = models.TextField(blank=True)
	description = models.TextField(blank=True)
	status      = models.CharField(default='active', max_length=50, blank=False) # active, inactive, passed
	
	# Backup Fields
	trash       = models.BooleanField(default=False)

	def __str__(self):
		return self.note_id