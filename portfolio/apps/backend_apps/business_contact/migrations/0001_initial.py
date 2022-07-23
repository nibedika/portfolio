# Generated by Django 2.2.4 on 2022-06-16 16:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend_access', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('contact_id', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=100, validators=[django.core.validators.EmailValidator])),
                ('subject', models.CharField(max_length=150)),
                ('text', models.TextField(blank=True)),
                ('file', models.FileField(blank=True, upload_to='')),
                ('status', models.CharField(default='unseen', max_length=50, validators=[django.core.validators.RegexValidator])),
                ('trash', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_user_id', to='backend_access.User')),
            ],
        ),
    ]
