# Generated by Django 2.2.4 on 2022-06-16 16:30

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
            name='Contact_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('list_id', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('remark', models.TextField(blank=True)),
                ('status', models.CharField(default='active', max_length=50, validators=[django.core.validators.RegexValidator])),
                ('trash', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sms_marketing_list_user', to='backend_access.User')),
            ],
        ),
        migrations.CreateModel(
            name='Cl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sms_id', models.CharField(max_length=50)),
                ('sender_contact', models.CharField(max_length=150)),
                ('text', models.TextField(blank=True)),
                ('status', models.CharField(default='unseen', max_length=50, validators=[django.core.validators.RegexValidator])),
                ('trash', models.BooleanField(default=False)),
                ('receiver_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_sms', to='sms_marketing.Contact_list')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sms_marketing_user', to='backend_access.User')),
            ],
        ),
    ]
