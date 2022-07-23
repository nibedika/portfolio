from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator


# Create your models here.
class User(models.Model):

	# General Info Fields
	date             = models.DateTimeField(auto_now_add=True)
	user_id          = models.CharField(max_length=50, blank=False)
	name             = models.CharField(max_length=50, blank=False)
	username         = models.SlugField(validators=[RegexValidator], max_length=50, blank=False)
	email            = models.EmailField(validators=[EmailValidator], max_length=100, blank=False)
	password         = models.CharField(validators=[RegexValidator], max_length=255, blank=False)
	confirmed_pass   = models.CharField(validators=[RegexValidator], max_length=255, blank=False)
	birthday         = models.DateTimeField(auto_now_add=True)
	gender           = models.CharField(validators=[RegexValidator], max_length=20, blank=False)
	
	account_type     = models.SlugField(validators=[RegexValidator], max_length=50, blank=False) #option-> dev, account, admin
	admin_auth       = models.ForeignKey("self", on_delete=models.CASCADE, related_name='backend_admin_auth') #For Business Admin
	designation      = models.SlugField(validators=[RegexValidator], max_length=50, blank=False)

	# Contact Info Filds
	contact_no       = models.CharField(max_length=50, blank=False)
	address          = models.TextField(validators=[RegexValidator], blank=True)
	city             = models.CharField(validators=[RegexValidator], max_length=255, blank=False)
	country          = models.CharField(validators=[RegexValidator], max_length=255, blank=False)
	available_in     = models.TextField(validators=[RegexValidator], blank=True)
	available_for    = models.TextField(validators=[RegexValidator], blank=True)
	
	# Identity Info Fields
	intro            = models.TextField(validators=[RegexValidator], blank=True)
	profile_img      = models.ImageField(height_field=None, width_field=None, max_length=100, blank=True)
	display_pic      = models.ImageField(height_field=None, width_field=None, max_length=100, blank=True)
	logo             = models.ImageField(height_field=None, width_field=None, max_length=100, blank=True)
	banner           = models.ImageField(height_field=None, width_field=None, max_length=100, blank=True)
	
	# Web Info Fields
	website          = models.TextField(validators=[RegexValidator], blank=True)
	facebook_link    = models.TextField(validators=[RegexValidator], blank=True)
	instagram_link   = models.TextField(validators=[RegexValidator], blank=True)
	whatsup_link     = models.TextField(validators=[RegexValidator], blank=True)
	twitter_link     = models.TextField(validators=[RegexValidator], blank=True)
	google_link      = models.TextField(validators=[RegexValidator], blank=True)
	youtube_link     = models.TextField(validators=[RegexValidator], blank=True)
	linkedin_link    = models.TextField(validators=[RegexValidator], blank=True)
	pinterest_link   = models.TextField(validators=[RegexValidator], blank=True)
	tumblr_link      = models.TextField(validators=[RegexValidator], blank=True)
	other_link       = models.TextField(validators=[RegexValidator], blank=True)
	
	# Status Fields
	info_verified    = models.BooleanField(default=False)
	email_verified   = models.BooleanField(default=False)
	account_verified = models.BooleanField(default=False)
	
	status           = models.CharField(validators=[RegexValidator], max_length=50, default='active') #option-> active, suspend, band, behold
	
	# Backup Fields
	trash            = models.BooleanField(default=False)
	
	def __str__(self):
		return self.user_id

