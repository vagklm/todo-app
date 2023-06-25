from django.urls import path
from . import views

urlpatterns = [
    path('simple_project/', views.simple_project, name='simple_project'),
]