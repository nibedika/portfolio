from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension

from apps.access_apps.backend_access.models import User as backendUser


# Create your models here.
class Admin_cl(models.Model):

	# General Info Fields
	date          = models.DateTimeField(auto_now_add=True)
	privilege_id  = models.CharField(max_length=50, blank=False)
	
	auth_id       = models.ForeignKey(backendUser, on_delete=models.CASCADE, related_name='privilege_admin_auth_id')
	admin_id      = models.ForeignKey(backendUser, on_delete=models.CASCADE, related_name='privilege_admin_id')
	
	component     = models.CharField(max_length=150, blank=False)
	position      = models.IntegerField(blank=True, null=True)
	view_action   = models.BooleanField(default=False)
	edit_action   = models.BooleanField(default=False)
	delete_action = models.BooleanField(default=False)
	
	status        = models.CharField(default='active', max_length=50, blank=False) # active, inactive
	
	# Backup Fields
	trash         = models.BooleanField(default=False)

	def __str__(self):
		return self.privilege_id




# class Feature_Cl(models.Model):
	
# 	privilege_id  = models.ForeignKey(Admin_Cl, on_delete=models.CASCADE, related_name='privilege_id')
	
# 	component     = models.CharField(max_length=150, blank=False)
# 	view_action   = models.BooleanField(default=False)
# 	edit_action   = models.BooleanField(default=False)
# 	delete_action = models.BooleanField(default=False)
	
# 	# Backup Fields
# 	trash         = models.BooleanField(default=False)

# 	def __str__(self):
# 		return self.privilege_id
