from django.urls import path
from apps.backend_apps.privilege import views
 
urlpatterns = [
    path('all-privilege/', views.Privilege.privilege_all, name='privilege_all'),
    path('generate-privilege/<userId>/', views.Privilege.generate_privilege, name='generate_privilege'),
    path('set-privilege/<userId>/', views.Privilege.set_privilege, name='set_privilege'),
]