from django.urls import path
from apps.frontend_apps.service import views
 
urlpatterns = [
    path('add-service/<confirmation>/', views.Service.service_add, name='service_add'),
    path('all-service/<confirmation>/', views.Service.service_all, name='service_all'),
    path('view-service/<id>/', views.Service.service_view, name='service_view'),
    path('edit-service/<id>/', views.Service.service_edit, name='service_edit'),
    path('delete-service/<id>/', views.Service.service_delete, name='service_delete'),
]