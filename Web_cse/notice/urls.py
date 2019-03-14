
from django.urls import path
from . import views


app_name = 'notice'
urlpatterns = [
    path('', views.home, name='home'),
    path('filteredQuery/', views.filter_query, name='filter_query'),
    path('<int:notice_id>/notice/', views.output_notice, name='output_notice')
]




