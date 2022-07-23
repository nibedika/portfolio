from django.urls import path
from apps.frontend_apps.portfolio import views
 
urlpatterns = [
    path('add-portfolio-act/<confirmation>/', views.Portfolio.portfolio_add, name='portfolio_add'),
    path('all-portfolio-act/<confirmation>/', views.Portfolio.portfolio_all, name='portfolio_all'),
    path('view-portfolio-act/<id>/', views.Portfolio.portfolio_view, name='portfolio_view'),
    path('edit-portfolio-act/<id>/', views.Portfolio.portfolio_edit, name='portfolio_edit'),
    path('delete-portfolio-act/<id>/', views.Portfolio.portfolio_delete, name='portfolio_delete'),
]