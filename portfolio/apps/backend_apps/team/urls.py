from django.urls import path
from apps.backend_apps.team import views
 
urlpatterns = [
	path('add-member/<confirmation>/', views.Team.member_add, name='member_add'),
    path('all-member/<confirmation>/', views.Team.member_all, name='member_all'),
    path('view-member/<id>/', views.Team.member_view, name='member_view'),
    path('edit-member/<id>/', views.Team.member_edit, name='member_edit'),
    path('delete-member/<id>/', views.Team.member_delete, name='member_delete'),

    path('add-team/<confirmation>/', views.Team.team_add, name='team_add'),
    path('all-team/<confirmation>/', views.Team.team_all, name='team_all'),
    path('view-team/<id>/', views.Team.team_view, name='team_view'),
    path('edit-team/<id>/', views.Team.team_edit, name='team_edit'),
    path('delete-team/<id>/', views.Team.team_delete, name='team_delete'),
]