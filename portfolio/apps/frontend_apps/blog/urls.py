from django.urls import path
from apps.frontend_apps.blog import views
 
urlpatterns = [
    path('add-blog/<confirmation>/', views.Blog.blog_add, name='blog_add'),
    path('all-blog/<confirmation>/', views.Blog.blog_all, name='blog_all'),
    path('view-blog/<id>/', views.Blog.blog_view, name='blog_view'),
    path('edit-blog/<id>/', views.Blog.blog_edit, name='blog_edit'),
    path('delete-blog/<id>/', views.Blog.blog_delete, name='blog_delete'),
]