# Generated by Django 2.2.4 on 2022-06-16 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend_access', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_cl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('privilege_id', models.CharField(max_length=50)),
                ('component', models.CharField(max_length=150)),
                ('position', models.IntegerField(blank=True, null=True)),
                ('view_action', models.BooleanField(default=False)),
                ('edit_action', models.BooleanField(default=False)),
                ('delete_action', models.BooleanField(default=False)),
                ('status', models.CharField(default='active', max_length=50)),
                ('trash', models.BooleanField(default=False)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='privilege_admin_id', to='backend_access.User')),
                ('auth_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='privilege_admin_auth_id', to='backend_access.User')),
            ],
        ),
    ]