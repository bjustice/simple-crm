from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'mycrm'
urlpatterns = [

    #record
    path('record', views.select_type, name='select-record-type'),
    
    path('record/group/<int:group_id>', views.post_record, name='add-record'),
    path('record/<int:record_id>', views.detail, name='detail'),
    path('summary', views.summary, name='summary'),
    
    #record group
    path('recordgroup', views.post_record_group, name='add-record-group'),
    path('company', views.post_company, name='add-company'),

    path('login', views.sign_in, name='sign-in'),
    path('signup', views.sign_up, name='sign-up'),
    
    path('home', views.home, name='home'),
    path('dash', views.dash, name='dash'),


    path('dataloader', views.data_loader, name='data=loader'),
    
    path("logout", LogoutView.as_view(), name="logout"),
    path('buttons', views.buttons, name='buttons'),
    path('settings', views.settings, name='settings'),
    path('forms', views.forms, name='forms'),
    path('modals', views.modals, name='modals'),
    path('bootstrap-tables', views.bootstrap_tables, name='bootstrap_tables'),
]