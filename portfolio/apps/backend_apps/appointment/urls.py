from django.urls import path
from apps.backend_apps.appointment import views
 
urlpatterns = [
    path('add-appointment/<confirmation>/', views.Appointment.appointment_add, name='appointment_add'),
    path('all-appointment/<confirmation>/', views.Appointment.appointment_all, name='appointment_all'),
    path('edit-appointment/<id>/', views.Appointment.appointment_edit, name='appointment_edit'),
    path('delete-appointment/<id>/', views.Appointment.appointment_delete, name='appointment_delete'),
]