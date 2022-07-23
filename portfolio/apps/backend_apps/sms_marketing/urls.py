from django.urls import path
from apps.backend_apps.sms_marketing import views
 
urlpatterns = [
    path('contact-list/<confirmation>/', views.SMS_marketing.contact_list, name='contact_list'),
    path('edit-contact/<id>/', views.SMS_marketing.contact_edit, name='contact_edit'),
    path('delete-contact/<id>/', views.SMS_marketing.contact_delete, name='contact_delete'),

    path('marketing-sms-send/<confirmation>/', views.SMS_marketing.marketing_sms_send, name='marketing_sms_send'),
    path('marketing-sms-all/<confirmation>/', views.SMS_marketing.marketing_sms_all, name='marketing_sms_all'),
    path('marketing-sms-delete/<id>/', views.SMS_marketing.marketing_sms_delete, name='marketing_sms_delete'),
]