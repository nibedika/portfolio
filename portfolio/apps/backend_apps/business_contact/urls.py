from django.urls import path
from apps.backend_apps.business_contact import views
 
urlpatterns = [
    path('view-business-contact/<contactId>/', views.Business_contact.business_contact_view, name='business_contact_view'),
    path('all-business-contact/<confirmation>/', views.Business_contact.business_contact_all, name='business_contact_all'),
    #path('view-business-contact/<id>/', views.Business_contact.business_contact_view, name='business_contact_view'),
    #path('delete-business-contact/<id>/', views.Business_contact.business_contact_delete, name='business_contact_delete'),
]