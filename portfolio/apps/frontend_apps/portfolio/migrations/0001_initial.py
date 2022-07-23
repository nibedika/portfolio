# Generated by Django 2.2.4 on 2022-06-16 16:36

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
                ('portfolio_id', models.CharField(max_length=50)),
                ('portfolio_topic', models.CharField(max_length=100)),
                ('portfolio_title', models.TextField(blank=True)),
                ('portfolio_txt', models.TextField(blank=True)),
                ('portfolio_img', models.FileField(blank=True, upload_to='')),
                ('status', models.CharField(default='inactive', max_length=180, validators=[django.core.validators.RegexValidator])),
                ('trash', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_user_id', to='backend_access.User')),
            ],
        ),
    ]
