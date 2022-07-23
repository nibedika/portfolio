from django.urls import path
from apps.frontend_apps.user_contact import views
 
urlpatterns = [
    path('add-user-contact/<userId>/<confirmation>/', views.User_contact.user_contact_add, name='user_contact_add'),
]