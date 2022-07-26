# Generated by Django 2.2.4 on 2022-06-16 16:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('username', models.SlugField(validators=[django.core.validators.RegexValidator])),
                ('email', models.EmailField(max_length=100, validators=[django.core.validators.EmailValidator])),
                ('password', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator])),
                ('confirmed_pass', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator])),
                ('birthday', models.DateTimeField(auto_now_add=True)),
                ('gender', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator])),
                ('account_type', models.SlugField(validators=[django.core.validators.RegexValidator])),
                ('designation', models.SlugField(validators=[django.core.validators.RegexValidator])),
                ('contact_no', models.CharField(max_length=50)),
                ('address', models.TextField(blank=True, validators=[django.core.validators.RegexValidator])),
                ('city', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator])),
                ('country', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator])),
                ('available_in', models.TextField(blank=True, validators=[django.core.validators.RegexValidator])),
                ('available_for', models.TextField(blank=True, validators=[django.core.validators.RegexValidator])),
                ('intro', models.TextField(blank=True, validators=[django.core.validators.RegexValidator])),
                ('profile_img', models.ImageField(blank=True, upload_to='')),
                ('display_pic', models.ImageField(blank=True, upload_to='')),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('banner', models.ImageField(blank=True, upload_to='')),
                ('website', models.TextField(blank=True, validators=[django.core.validators.RegexValidator])),
                ('facebook_link', models.TextField(blank=True, validators=[django.core.validators.RegexValidator])),
                ('instagram_link', models.TextField(blank=True, validators=[django.core.validators.RegexValidator])),
                ('whatsup_link', models.TextField(blank=True, validators=[django.core.validators.RegexValidator])),
                ('twitter_link', models.TextField(blank=True, validators=[django.core.validators.RegexValidator])),
                ('google_link', models.TextField(blank=True, validators=[django.core.validators.RegexValidator])),
                ('youtube_link', models.TextField(blank=True, validators=[django.core.validators.RegexValidator])),
                ('linkedin_link', models.TextField(blank=True, validators=[django.core.validators.RegexValidator])),
                ('pinterest_link', models.TextField(blank=True, validators=[django.core.validators.RegexValidator])),
                ('tumblr_link', models.TextField(blank=True, validators=[django.core.validators.RegexValidator])),
                ('other_link', models.TextField(blank=True, validators=[django.core.validators.RegexValidator])),
                ('info_verified', models.BooleanField(default=False)),
                ('email_verified', models.BooleanField(default=False)),
                ('account_verified', models.BooleanField(default=False)),
                ('status', models.CharField(default='active', max_length=50, validators=[django.core.validators.RegexValidator])),
                ('trash', models.BooleanField(default=False)),
                ('admin_auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='backend_admin_auth', to='backend_access.User')),
            ],
        ),
    ]
