from django.urls import path
from apps.backend_apps.additional_income import views
 
urlpatterns = [
    path('add-additional-income-field/<confirmation>/', views.Additional_income.additional_income_field_add, name='additional_income_field_add'),
    path('edit-additional-income-field/<id>/', views.Additional_income.additional_income_field_edit, name='additional_income_field_edit'),
    path('delete-additional-income-field/<id>/', views.Additional_income.additional_income_field_delete, name='additional_income_field_delete'),

    path('add-additional-income/<confirmation>/', views.Additional_income.additional_income_add, name='additional_income_add'),
    path('all-additional-income/<confirmation>/', views.Additional_income.additional_income_all, name='additional_income_all'),
    path('view-additional-income/<id>/', views.Additional_income.additional_income_view, name='additional_income_view'),
    path('edit-additional-income/<id>/', views.Additional_income.additional_income_edit, name='additional_income_edit'),
    path('delete-additional-income/<id>/', views.Additional_income.additional_income_delete, name='additional_income_delete'),
]