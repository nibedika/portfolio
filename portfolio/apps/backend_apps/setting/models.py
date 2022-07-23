from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator

from apps.access_apps.backend_access.models import User as backendUser


# Create your models here.
class Rules_cl(models.Model):

	# General Info Fields
	date          = models.DateTimeField(auto_now_add=True)
	rules_id      = models.CharField(max_length=50, blank=False)
	user_id       = models.ForeignKey(backendUser, on_delete=models.CASCADE, related_name='rules_user_id')
	
	preference    = models.TextField(validators=[RegexValidator], blank=True)
	conditions    = models.TextField(validators=[RegexValidator], blank=True)
	authorised_by = models.CharField(max_length=50, blank=False)
	
	status        = models.CharField(default='active', max_length=50, blank=False) # active, inactive
	
	# Backup Fields
	trash         = models.BooleanField(default=False)

	def __str__(self):
		return self.rules_id




class Website_cl(models.Model):

	# General Info Fields
	date        = models.DateTimeField(auto_now_add=True)
	website_id  = models.CharField(max_length=50, blank=False)
	user_id     = models.ForeignKey(backendUser, on_delete=models.CASCADE, related_name='website_user_id')
	
	slider_img1 = models.ImageField(height_field=None, width_field=None, max_length=100, blank=True)
	slider_txt1 = models.TextField(validators=[RegexValidator], blank=True)
	
	slider_img2 = models.ImageField(height_field=None, width_field=None, max_length=100, blank=True)
	slider_txt2 = models.TextField(validators=[RegexValidator], blank=True)
	
	slider_img3 = models.ImageField(height_field=None, width_field=None, max_length=100, blank=True)
	slider_txt3 = models.TextField(validators=[RegexValidator], blank=True)
	
	cv_file     = models.ImageField(height_field=None, width_field=None, max_length=100, blank=True)
	
	about_img   = models.ImageField(height_field=None, width_field=None, max_length=100, blank=True)
	about_txt   = models.TextField(validators=[RegexValidator], blank=True)
	
	status      = models.CharField(default='active', max_length=50, blank=False) # active, inactive
	
	# Backup Fields
	trash       = models.BooleanField(default=False)

	def __str__(self):
		return self.website_id
