from django.urls import path
from apps.backend_apps.metting import views
 
urlpatterns = [
    path('add-metting/<confirmation>/', views.Metting.metting_add, name='metting_add'),
    path('all-metting/<confirmation>/', views.Metting.metting_all, name='metting_all'),
    path('edit-metting/<id>/', views.Metting.metting_edit, name='metting_edit'),
    path('delete-metting/<id>/', views.Metting.metting_delete, name='metting_delete'),
]