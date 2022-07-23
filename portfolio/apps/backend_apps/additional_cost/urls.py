from django.urls import path
from apps.backend_apps.additional_cost import views
 
urlpatterns = [
    path('add-additional-cost-field/<confirmation>/', views.Additional_cost.additional_cost_field_add, name='additional_cost_field_add'),
    path('edit-additional-cost-field/<id>/', views.Additional_cost.additional_cost_field_edit, name='additional_cost_field_edit'),
    path('delete-additional-cost-field/<id>/', views.Additional_cost.additional_cost_field_delete, name='additional_cost_field_delete'),

    path('add-additional-cost/<confirmation>/', views.Additional_cost.additional_cost_add, name='additional_cost_add'),
    path('all-additional-cost/<confirmation>/', views.Additional_cost.additional_cost_all, name='additional_cost_all'),
    path('view-additional-cost/<id>/', views.Additional_cost.additional_cost_view, name='additional_cost_view'),
    path('edit-additional-cost/<id>/', views.Additional_cost.additional_cost_edit, name='additional_cost_edit'),
    path('delete-additional-cost/<id>/', views.Additional_cost.additional_cost_delete, name='additional_cost_delete'),
]