from django.urls import path
from apps.access_apps.backend_access import views
 
urlpatterns = [
    path('sign-up/', views.Backend_access.sign_up, name='sign_up'),
    path('email-verify/<emailCode>/<email>/<confirmation>/', views.Backend_access.email_verify, name='email_verify'),
    path('sign-in/', views.Backend_access.sign_in, name='sign_in'),
    path('home/', views.Backend_access.home, name='home'),
    path('sign-out/', views.Backend_access.sign_out, name='sign_out'),

    path('password-recovery-surface/', views.Backend_access.password_recovery_surface, name='password_recovery_surface'),
    path('password-recovery-code/', views.Backend_access.password_recovery_code, name='password_recovery_code'),
    path('password-recovery/', views.Backend_access.password_recovery, name='password_recovery'),
    path('account-setting/', views.Backend_access.account_setting, name='account_setting'),
    path('all-account/', views.Backend_access.all_account, name='all_account'),
]