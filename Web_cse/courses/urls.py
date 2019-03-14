from django.urls import path
from . import views


app_name = 'courses'

urlpatterns = [
    path('', views.course_view, name='course_view'),
]
