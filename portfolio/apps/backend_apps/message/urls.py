from django.urls import path
from apps.backend_apps.message import views
 
urlpatterns = [
    path('add-message/<confirmation>/', views.Message.message_add, name='message_add'),
    path('all-message/<confirmation>/', views.Message.message_all, name='message_all'),
    path('view-message/<id>/', views.Message.message_view, name='message_view'),
    path('delete-message/<id>/', views.Message.message_delete, name='message_delete'),
]