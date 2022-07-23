from django.urls import path
from apps.access_apps.frontend_access import views
 
urlpatterns = [
    # path('web/', views.Frontend_access.web_home, name='web'),
    path('', views.Frontend_access.web_home, name='web'),

    path('portfolio-detail/<portfolioId>/', views.Frontend_access.portfolio_detail, name='portfolio_detail'),
    path('blog-detail/<blogId>/', views.Frontend_access.blog_detail, name='blog_detail'),
]