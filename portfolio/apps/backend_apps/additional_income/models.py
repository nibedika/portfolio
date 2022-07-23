from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension

from apps.access_apps.backend_access.models import User as backendUser


# Create your models here.
class Field_cl(models.Model):

	# General Info Fields
	date     = models.DateTimeField(auto_now_add=True)
	field_id = models.CharField(max_length=50, blank=False)
	user_id  = models.ForeignKey(backendUser, on_delete=models.CASCADE, related_name='income_field_user_id')
	title    = models.TextField(blank=True)
	slug     = models.SlugField(validators=[RegexValidator], max_length=255, blank=False)
	status   = models.CharField(default='active', max_length=50, blank=False) # active, inactive
	
	# Backup Fields
	trash    = models.BooleanField(default=False)

	def __str__(self):
		return self.field_id



class Cl(models.Model):

	# General Info Fields
	date        = models.DateTimeField(auto_now_add=True)
	income_id   = models.CharField(max_length=50, blank=False)
	user_id     = models.ForeignKey(backendUser, on_delete=models.CASCADE, related_name='income_user_id')
	field_id    = models.ForeignKey(Field_cl, on_delete=models.CASCADE, related_name='income_field_id')
	amount      = models.DecimalField(max_digits=99, decimal_places=3, blank=True)
	description = models.TextField(blank=True)
	earn_by     = models.CharField(max_length=250, blank=False)
	status      = models.CharField(default='active', max_length=50, blank=False) # active, inactive
	
	# Backup Fields
	trash       = models.BooleanField(default=False)

	def __str__(self):
		return self.income_id