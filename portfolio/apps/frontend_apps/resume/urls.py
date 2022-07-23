from django.urls import path
from apps.frontend_apps.resume import views
 
urlpatterns = [
    path('add-resume/<confirmation>/', views.Resume.resume_add, name='resume_add'),
    path('all-resume/<confirmation>/', views.Resume.resume_all, name='resume_all'),
    path('view-resume/<id>/', views.Resume.resume_view, name='resume_view'),
    path('edit-resume/<id>/', views.Resume.resume_edit, name='resume_edit'),
    path('delete-resume/<id>/', views.Resume.resume_delete, name='resume_delete'),
]