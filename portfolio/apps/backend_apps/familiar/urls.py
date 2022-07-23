from django.urls import path
from apps.backend_apps.familiar import views
 
urlpatterns = [

    path('familiar-add/<confirmation>/', views.Familiar.familiar_add, name='familiar_add'),
    path('familiar-all/<confirmation>/', views.Familiar.familiar_all, name='familiar_all'),
    path('familiar-view/<id>/', views.Familiar.familiar_view, name='familiar_view'),
    path('familiar-edit/<id>/', views.Familiar.familiar_edit, name='familiar_edit'),
    path('familiar-delete/<id>/', views.Familiar.familiar_delete, name='familiar_delete'),
    
]