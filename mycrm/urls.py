from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'mycrm'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('login', views.sign_in, name='work'),
    path('signup', views.sign_up, name='sign-up'),
    
    path('home', views.home, name='home'),
    path('dash', views.dash, name='dash'),
    path('record', views.post_record, name='add-record'),
    path('summary', views.summary, name='summary'),
    path('record/<int:record_id>', views.detail, name='detail'),

    path("logout", LogoutView.as_view(), name="logout"),
    path('dashboard', views.dashboard, name='dashboard'),
    path('bootstrap-tables', views.bootstrap_tables, name='bootstrap_tables'),
]