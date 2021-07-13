from django.urls import path

from . import views

app_name = 'mycrm'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /mycrm/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /mycrm/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /mycrm/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]