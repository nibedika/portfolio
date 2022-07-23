from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator

from apps.access_apps.backend_access.models import User as userDB


# Create your models here.
class Cl(models.Model):

	# General Info Fields
	date       = models.DateTimeField(auto_now_add=True)
	blog_id    = models.CharField(max_length=50, blank=False)
	
	blog_title = models.TextField(blank=True)
	blog_txt   = models.TextField(blank=True)
	blog_img   = models.FileField(max_length=100, blank=True)
	blog_link  = models.TextField(blank=True)
	
	publisher  = models.ForeignKey(userDB, on_delete=models.CASCADE, related_name='blog_publisher')
	status     = models.CharField(validators=[RegexValidator], max_length=180, default='inactive') #option-> active, inactive 
	
	# Backup Fields
	trash      = models.BooleanField(default=False)
	
	def __str__(self):
		return self.blog_id
