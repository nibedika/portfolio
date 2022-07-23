from django.urls import path
from apps.backend_apps.setting import views
 
urlpatterns = [
    path('rules-setting/<confirmation>/', views.Setting.rules_setting, name='rules_setting'),
    path('view-rules/<id>/', views.Setting.rules_view, name='rules_view'),
    path('edit-rules/<id>/', views.Setting.rules_edit, name='rules_edit'),
    path('delete-rules/<id>/', views.Setting.rules_delete, name='rules_delete'),

    path('website-setting/<confirmation>/', views.Setting.website_setting, name='website_setting'),
]