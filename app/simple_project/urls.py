from django.urls import path
from simple_project import views

urlpatterns = [
    path('', views.simple_project, name='simple_project'),
]