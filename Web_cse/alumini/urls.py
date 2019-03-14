from django.urls import path
from . import views

app_name = 'alumini'
urlpatterns = [
    path('', views.alumini_search, name='alumini_search'),
    path('searchByname/', views.name_search, name='name_search'),
    path('searchByroll/', views.roll_search, name='roll_search'),
    path('batchView/', views.alumini_search_batch, name='alumini_search_batch'),
    path('batchView/search', views.BatchView, name='BatchView')
]


