from django.urls import path
from apps.backend_apps.note import views
 
urlpatterns = [
    path('add-note/<confirmation>/', views.Note.note_add, name='note_add'),
    path('all-note/<confirmation>/', views.Note.note_all, name='note_all'),
    path('edit-note/<id>/', views.Note.note_edit, name='note_edit'),
    path('delete-note/<id>/', views.Note.note_delete, name='note_delete'),
]