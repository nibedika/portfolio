from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension

from apps.access_apps.backend_access.models import User as backendUser


# Create your models here.
class Member_cl(models.Model):

	# General Info Fields
	date         = models.DateTimeField(auto_now_add=True)
	member_id    = models.CharField(max_length=50, blank=False)
	user_id      = models.ForeignKey(backendUser, on_delete=models.CASCADE, related_name='member_user_id')
	
	name         = models.CharField(max_length=250, blank=True)
	email        = models.EmailField(validators=[EmailValidator], max_length=100, blank=True)
	contact_no   = models.CharField(max_length=50, blank=False)
	address      = models.TextField(blank=True)
	description  = models.TextField(blank=True)
	remark       = models.TextField(blank=True)
	image        = models.FileField(max_length=100, blank=True)
	
	member_type  = models.CharField(default='none', max_length=50, blank=False) # full_time, part_time
	shift        = models.CharField(max_length=150, blank=False)
	designation  = models.SlugField(validators=[RegexValidator], max_length=155, blank=False)
	salary       = models.DecimalField(max_digits=99, decimal_places=3, blank=True)
	joining_date = models.DateTimeField(auto_now_add=True, blank=False)
	leaving_date = models.DateTimeField(auto_now_add=False, blank=True)
	
	status       = models.CharField(default='active', max_length=50, blank=False) # active, vacation, suspended, fired, quited
	
	# Backup Fields
	trash        = models.BooleanField(default=False)

	def __str__(self):
		return self.member_id




class Cl(models.Model):

	# General Info Fields
	date        = models.DateTimeField(auto_now_add=True)
	user_id     = models.ForeignKey(backendUser, on_delete=models.CASCADE, related_name='team_user_id')
	team_id     = models.CharField(max_length=50, blank=False)
	
	team_head   = models.ForeignKey(Member_cl, on_delete=models.CASCADE, related_name='team_head_id')
	member_id   = models.ManyToManyField(Member_cl, related_name='team_member_ids', blank=True)

	team_name   = models.CharField(max_length=250, blank=False)
	description = models.TextField(blank=True)
	remark      = models.TextField(blank=True)
	
	status      = models.CharField(default='active', max_length=50, blank=False) # active, inactive
	
	# Backup Fields
	trash       = models.BooleanField(default=False)

	def __str__(self):
		return self.team_id