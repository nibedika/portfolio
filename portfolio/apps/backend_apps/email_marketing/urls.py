from django.urls import path
from apps.backend_apps.email_marketing import views
 
urlpatterns = [
    path('email-list/<confirmation>/', views.Email_marketing.email_list, name='email_list'),
    path('edit-email/<id>/', views.Email_marketing.email_edit, name='email_edit'),
    path('delete-email/<id>/', views.Email_marketing.email_delete, name='email_delete'),

    path('marketing-email-send/<confirmation>/', views.Email_marketing.marketing_email_send, name='marketing_email_send'),
    path('marketing-email-all/<confirmation>/', views.Email_marketing.marketing_email_all, name='marketing_email_all'),
    path('marketing-email-delete/<id>/', views.Email_marketing.marketing_email_delete, name='marketing_email_delete'),
]