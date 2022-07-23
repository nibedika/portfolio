"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# For Media URL
from django.conf import settings
from django.conf.urls.static import static
#from package.internal import ajax_helper

from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [

    # Ajax Helper Url For AngularJS 
    #path('ajaxHelper/', ajax_helper.Ajax_helper, name='ajaxHelper'),
    #path('ajaxHelper/getData/', ajax_helper.Ajax_helper.getData, name='ajaxHelper/getData/'),


    # Access App's Urls
    path('backend-access/', include('apps.access_apps.backend_access.urls'), name='backend_access'),
    #path('frontend-access/', include('apps.access_apps.frontend_access.urls'), name='frontend_access'),
    path('', include('apps.access_apps.frontend_access.urls'), name='frontend_access'),


    # # Backend Business App's Urls
    # path('report/', include('apps.backend_apps.report.urls'), name='report'),
    path('appointment/', include('apps.backend_apps.appointment.urls'), name='appointment'),
    path('metting/', include('apps.backend_apps.metting.urls'), name='metting'),
    path('note/', include('apps.backend_apps.note.urls'), name='note'),
    path('familiar/', include('apps.backend_apps.familiar.urls'), name='familiar'),
    path('team/', include('apps.backend_apps.team.urls'), name='team'),
    path('additional-income/', include('apps.backend_apps.additional_income.urls'), name='additional_income'),
    path('additional-cost/', include('apps.backend_apps.additional_cost.urls'), name='additional_cost'),
    
    path('email-marketing/', include('apps.backend_apps.email_marketing.urls'), name='email_marketing'),
    path('sms-marketing/', include('apps.backend_apps.sms_marketing.urls'), name='sms_marketing'),
    path('business-contact/', include('apps.backend_apps.business_contact.urls'), name='business_contact'),
    path('message/', include('apps.backend_apps.message.urls'), name='message'),
    path('privilege/', include('apps.backend_apps.privilege.urls'), name='privilege'),
    path('setting/', include('apps.backend_apps.setting.urls'), name='setting'),


    # Frontend App's Urls
    path('resume/', include('apps.frontend_apps.resume.urls'), name='resume'),
    path('portfolio/', include('apps.frontend_apps.portfolio.urls'), name='portfolio'),
    path('service/', include('apps.frontend_apps.service.urls'), name='service'),
    path('blog/', include('apps.frontend_apps.blog.urls'), name='blog'),
    path('user-contact/', include('apps.frontend_apps.user_contact.urls'), name='user_contact'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.COMPRESS_ROOT)
